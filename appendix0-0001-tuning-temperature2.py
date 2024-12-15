from openai import OpenAI
from google.colab import userdata

api_key = userdata.get('openai_key')

client = OpenAI(api_key=api_key)

MODEL = "gpt-4o"

response = client.chat.completions.create(
    
    model=MODEL,

    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant"
        },
        {
            "role": "user",
            "content": "Please explain what a Martian is in three paragraphs"
        }
    ],
    temperature=1.7,

)

print(response.choices[0].message.content)

"""
non-sense response:)

"""
