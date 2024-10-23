# here => total_tokens=41

from openai import OpenAI
from google.colab import userdata

openai_key = userdata.get('openai_key')

client = OpenAI(api_key = openai_key)

# https://platform.openai.com/docs/models

completion = client.chat.completions.create(
    model = "gpt-4o",
    messages = [
        {"role": "system", "content": "You are an economist. Please, explain the terms in ten words or less."},
        {"role": "user", "content": "What is inflation?"}
    ]
)

print(completion.choices[0].message.content)

# cost!

print(completion.usage)

# CompletionUsage(completion_tokens=10, prompt_tokens=31, total_tokens=41, completion_tokens_details=CompletionTokensDetails(audio_tokens=None, reasoning_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=None, cached_tokens=0))

