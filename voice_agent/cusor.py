import asyncio
import json
import subprocess
import requests
import speech_recognition as sr
from dotenv import load_dotenv
from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)

# TOOLS 

def run_command(cmd: str):
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )
    return result.stdout or result.stderr

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Weather data unavailable"

available_tools = {
    "get_weather": get_weather,
    "weather": get_weather,
    "weather_api": get_weather,
    "weather_tool": get_weather,
    "run_command": run_command,
}

#  SYSTEM PROMPT 

SYSTEM_PROMPT = """
You are an AI agent that works step by step.

Steps:
START -> PLAN -> TOOL -> OBSERVED -> OUTPUT

Rules:
- Always respond in valid JSON
- Use TOOL step only when an external tool is required
- Use the tool name EXACTLY as one of the available tools
- You are running on Windows PowerShell

Available tools:
- get_weather(city: str)
- run_command(cmd: str)

JSON format:
{
  "step": "START | PLAN | TOOL | OBSERVED | OUTPUT",
  "content": "string",
  "tool": "string",
  "input": "string"
}
"""

def main():
    r = sr.Recognizer()
    r.pause_threshold = 2

    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    print("🎤 Voice Weather Agent started")
    print("Say 'exit' to stop\n")

    while True:
        #  VOICE INPUT 
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Speak Something...")
            audio = r.listen(source)

        try:
            user_text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("❌ Could not understand. Try again.\n")
            continue

        print("🗣️ You said:", user_text)

        if user_text.lower() == "exit":
            print("👋 Exiting agent")
            break

        message_history.append({"role": "user", "content": user_text})

        #  AGENT LOOP 
        while True:
            response = client.chat.completions.create(
                model="chatgpt-4o-latest",
                response_format={"type": "json_object"},
                messages=message_history
            )

            raw = response.choices[0].message.content
            parsed = json.loads(raw)
            step = parsed.get("step")

            message_history.append({"role": "assistant", "content": raw})

            if step in ("START", "PLAN"):
                print("🧠", parsed.get("content"))
                message_history.append(
                    {"role": "user", "content": "Continue to the next step."}
                )

            elif step == "TOOL":
                tool_name = parsed.get("tool", "")
                tool_input = parsed.get("input", "")
                normalized = tool_name.lower().replace("-", "_")

                print(f"⚒️ {tool_name}({tool_input})")

                if normalized in available_tools:
                    output = available_tools[normalized](tool_input)
                else:
                    output = f"Tool '{tool_name}' not available"

                message_history.append({
                    "role": "assistant",
                    "content": json.dumps({
                        "step": "OBSERVED",
                        "tool": normalized,
                        "input": tool_input,
                        "output": output
                    })
                })

            elif step == "OUTPUT":
                final_answer = parsed.get("content")
                print("🤖", final_answer, "\n")
                asyncio.run(tts(final_answer))
                break   

main()
