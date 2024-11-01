from openai import OpenAI
from google.colab import userdata

api_key = userdata.get("openai_key")

client = OpenAI(api_key = api_key)

image_url = "https://t3.ftcdn.net/jpg/07/46/74/96/360_F_746749607_zDV4D3BHULyb1NVvRVWujOSwNJWv8ufK.jpg"

response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "List the objects, human, animal etc in this picture."
                },
                {
                    "type": "image_url",
                    "image_url": {"url": image_url} # , "detail": "high" low, auto
                },
            ],
        }
    ],
    max_tokens = 150
)

print(response.choices[0].message.content)

"""
The picture shows a bird, specifically a starling, standing on a sandy surface. 
There are no other objects, humans, or animals visible in the image.
"""
