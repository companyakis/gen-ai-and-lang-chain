from openai import OpenAI
from google.colab import userdata

api_key = userdata.get('openai_key')

client = OpenAI(api_key=api_key)

audio_file = open("/content/samplespeech.mp3", "rb")
