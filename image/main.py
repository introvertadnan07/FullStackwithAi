from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role":"user",
            "content":[
                { "type": "text", "text": "Generate a caption for this image in about 50 words"},
                { "type": "image_url", "image_url": {"url": "https://images.pexels.com/photos/52608/pexels-photo-52608.jpeg?_gl=1*spajey*_ga*NTI5MzA5OTE5LjE3NjcyNDQzOTg.*_ga_8JE65Q40S6*czE3NjcyNDQzOTckbzEkZzEkdDE3NjcyNDQ3OTkkajI4JGwwJGgw"}}
            ]
        }
    ]
)

print("Response:", response.choices[0].message.content)