from openai import OpenAI
from google.colab import userdata

openai_key = userdata.get('openai_key')

client = OpenAI(api_key = openai_key)

url = "https://cdn.webrazzi.com/uploads/2024/08/trump-747.png"

response = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Give me some information about the photo. Who is he? Environment and people are important."},
                {
                    "type": "image_url",
                    "image_url": {"url": url},
                },
            ],
        }
    ],
    max_tokens = 250
)

print(response.choices[0].message.content)

# cost!

print(response.usage)

"""
I'm sorry, I can't tell who this person is. However, the image shows a man in a suit and red tie, gesturing with his hand. He's standing in front of a large American flag, suggesting that the setting might be a formal or political event. The environment is likely indoors given the size and display of the flag.
CompletionUsage(completion_tokens=67, prompt_tokens=1130, total_tokens=1197, completion_tokens_details=CompletionTokensDetails(audio_tokens=None, reasoning_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=1024))

"""
