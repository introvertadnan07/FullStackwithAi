# Robust Chain-of-Thought Weather Agent

from dotenv import load_dotenv
from openai import OpenAI
import json
import requests

load_dotenv()

client = OpenAI(base_url="https://api.openai.com/v1")

#  TOOLS 

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Weather data unavailable"

# Tool registry with aliases
available_tools = {
    "get_weather": get_weather,
    "weather": get_weather,
    "weather_api": get_weather,
    "weather_tool": get_weather,
}

# SYSTEM PROMPT 

SYSTEM_PROMPT = """
You are an AI agent that works step by step.

Steps:
START -> PLAN -> TOOL -> OBSERVED -> OUTPUT

Rules:
- Always respond in valid JSON
- Use TOOL step only when an external tool is required
- Use the tool name EXACTLY as one of the available tools

Available tools:
- get_weather(city: str)

JSON format:
{
  "step": "START | PLAN | TOOL | OBSERVED | OUTPUT",
  "content": "string",
  "tool": "string",
  "input": "string"
}
"""

print("\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("-> ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw})

    parsed = json.loads(raw)

    step = parsed.get("step")

    if step == "START":
        print("🔥", parsed.get("content"))
        message_history.append(
            {"role": "user", "content": "Continue to the next step."}
        )

    elif step == "PLAN":
        print("🧠", parsed.get("content"))
        message_history.append(
            {"role": "user", "content": "Continue to the next step."}
        )

    elif step == "TOOL":
        tool_name = parsed.get("tool", "")
        tool_input = parsed.get("input", "")

        normalized_tool = tool_name.lower().replace("-", "_")

        print(f"⚒️ {tool_name} ({tool_input})")

        if normalized_tool not in available_tools:
            tool_output = f"Tool '{tool_name}' is not available."
        else:
            tool_output = available_tools[normalized_tool](tool_input)

        message_history.append({
            "role": "assistant",
            "content": json.dumps({
                "step": "OBSERVED",
                "tool": normalized_tool,
                "input": tool_input,
                "output": tool_output
            })
        })

    elif step == "OUTPUT":
        print("🤖", parsed.get("content"))
        break

print("\n")
