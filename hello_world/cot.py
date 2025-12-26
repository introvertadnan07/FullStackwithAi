# Chain of Thought prompting

from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv() 

client = OpenAI(
    base_url="https://api.openai.com/v1"
)

SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user using chain of thought.
You work on START, PLAN and OUTPUT steps.

Rules:
- Strictly Follow the given JSON output format
- Only run one step at a time.
- The sequence of steps is START, PLAN and OUTPUT.

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content": "string"}
"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("-> ")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("🔥", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Continue to the next step."})
        continue

    if parsed_result.get("step") == "PLAN":
        print("🧠", parsed_result.get("content"))
        message_history.append({"role": "user", "content": "Continue to the next step."})
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("🤖", parsed_result.get("content"))
        break

print("\n\n\n")
