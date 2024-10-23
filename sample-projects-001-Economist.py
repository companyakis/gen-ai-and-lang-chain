from openai import OpenAI

OPENAI_API_KEY = ""

client = OpenAI(api_key = OPENAI_API_KEY)

# https://platform.openai.com/docs/models

completion = client.chat.completions.create(
  
    model = "gpt-4o",
    messages = [
        {"role": "system", "content": "You are an economist. Please, explain the terms in ten words or less."},
      
        {"role": "user", "content": "What is inflation?"}
    ]
)

print(completion.choices[0].message)

# ChatCompletionMessage(content='Increase in prices, reducing purchasing power of money.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)

