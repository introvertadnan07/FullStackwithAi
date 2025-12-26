# Few Shot Prompting 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.openai.com/v1"
)

SYSTEM_PROMPT = """

you should only ans the coding related question. Do not anything else. Your name is Alexa. if user something than coding, just say sorry.

Rule:
- Stricly follow the output in JSON format

Output Format:
{{
    "code": "string" or null,
    isCodingQuestion" : boolean
}}


Examples:

Q: Can you explain the a + b whole square?
A: {{"code": null, "isCodingQuestion": false}}

Q: Hey, Write a code in python for adding two numbers.
A: A: {{"code": def add(a, b):
          return a + b", "isCodingQuestion": false}}


"""

response = client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey, Can you explain a + b whole square"}
    ]
)

print(response.choices[0].message.content)