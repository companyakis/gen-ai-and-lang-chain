from openai import OpenAI
from google.colab import userdata
import base64

api_key = userdata.get('openai_key')

client = OpenAI(api_key=api_key)

# Function to encode the image

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "/content/vecihi.jpg" 

# Getting the base64 string
base64_image = encode_image(image_path)

MODEL = "gpt-4o"

response = client.chat.completions.create(
    model=MODEL,

    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Explain this photo."},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpg;base64,{base64_image}"},
                },
            ],
        }
    ],
    max_tokens=200,
)

print(response.choices[0].message.content)
