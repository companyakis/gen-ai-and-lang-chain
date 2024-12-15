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
            "content": "Please, explain what a Martian is"
        }
    ],
    temperature=0.6,
    max_tokens=200,
)

print(response.choices[0].message.content)

"""
A "Martian" is a term typically used to refer to a hypothetical or fictional inhabitant of the planet Mars. 
The concept of Martians has been popular in science fiction and popular culture for many years, often depicted as alien beings with various forms and characteristics. 
The idea of Martians originated when Mars was observed through telescopes in the 19th century, and some astronomers speculated about the possibility of life on the planet.

In literature and media, Martians have been portrayed in numerous ways, ranging from hostile invaders, 
as in H.G. Wells' "The War of the Worlds," to more benevolent or misunderstood creatures. 
While there is currently no evidence of life on Mars, the term "Martian" continues to capture the imagination of people as scientists explore 
the possibility of past or present life on the planet through missions and research.



"""
