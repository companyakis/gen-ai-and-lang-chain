from openai import OpenAI
from google.colab import userdata
from pathlib import Path

api_key = userdata.get('openai_key')

client = OpenAI(api_key=api_key)

# https://platform.openai.com/docs/guides/text-to-speech/quickstart
# https://platform.openai.com/docs/api-reference/audio/createSpeech

sample_speech_path = Path("__file__").parent/"samplespeech.mp3"
