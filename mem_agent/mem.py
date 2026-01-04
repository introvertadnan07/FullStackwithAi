from dotenv import load_dotenv
from mem0 import Memory
import json
import os
from openai import OpenAI

load_dotenv()

client = OpenAI()

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_KEY,
            "model": "text-embedding-3-small"
        }
    },
    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_KEY,
            "model": "gpt-4.1"
        }
    },
    "graph_store":{
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://55126cec.databases.neo4j.io",
            "username": "neo4j",
            "password" : "FuF64g4s-h2nSRybbiTAkpXwX7oDGfR5lonrt9sOHk4"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333
        }
    }
}

mem_client = Memory.from_config(config)

while True:
    user_query = input("> ")

    if user_query.lower() in {"exit", "quit"}:
        break

    search_memory = mem_client.search(
        query=user_query,
        user_id="anumifly"
    )

    memories = [
        f"Memory: {mem}"
        for mem in search_memory
    ]

    print("Found Memories:", memories)

    SYSTEM_PROMPT = f"""
Here is the context about the user:
{json.dumps(memories, indent=2)}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response = response.choices[0].message.content
    print("AI:", ai_response)

    mem_client.add(
        user_id="anumifly",
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory has been saved...\n")
