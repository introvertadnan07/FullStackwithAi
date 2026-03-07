import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI, AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI()
async_client = AsyncOpenAI()

class Message(BaseModel):
    text: str

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


@app.post("/chat")
async def chat(msg: Message):

    SYSTEM_PROMPT = """
You are an expert voice agent.
Respond naturally as a voice assistant.
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": msg.text}
        ]
    )

    ai_text = response.choices[0].message.content

    asyncio.create_task(tts(ai_text))

    return {"reply": ai_text}