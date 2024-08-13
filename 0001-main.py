# pip install python-dotenv

from dotenv import load_dotenv

import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

print(openai_key)

langchain_key = os.getenv("LANGCHAIN_API_KEY")

print(langchain_key)
