import asyncio
from dotenv import load_dotenv
import speech_recognition as sr
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

def main():
    r = sr.Recognizer()
    r.pause_threshold = 2

    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            print("Speak Something...")
            audio = r.listen(source)

        print("Processing Audio...(STT)")
        stt = r.recognize_google(audio)

        print("You said:", stt)

        SYSTEM_PROMPT = """
You are an expert voice agent.
You are given the transcript of what the user said.
Respond naturally as a voice assistant.
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt}
            ]
        )

        ai_text = response.choices[0].message.content
        print("AI Response:", ai_text)

        asyncio.run(tts(ai_text))

main()
 