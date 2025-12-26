from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.openai.com/v1"
)

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "system",
            "content": [
                {
                    "type": "input_text",
                    "text": "you are an expert in Maths and only and only answer maths related questions. If the query is not related to maths, just say sorry and do not answer."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Hey, can you help me solve the a + b whole square"
                }
            ]
        }
    ]
)

print(response.output_text)
