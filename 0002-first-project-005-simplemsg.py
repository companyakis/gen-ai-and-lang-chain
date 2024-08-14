from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=0.15
)

messages = [
    SystemMessage(content = "Please, translate the following sentence from English to Turkish."),

    HumanMessage(content = "A barking dog never bites!")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)
    #print(response.content)

"""

content='Havlayan köpek ısırmaz!' 
response_metadata={'token_usage': {'completion_tokens': 11, 'prompt_tokens': 29, 'total_tokens': 40}, 'model_name': 'gpt-4-0613', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} 
id='run-ed4e5c82-aabb-4164-b9d0-cfd4ced5609a-0' usage_metadata={'input_tokens': 29, 'output_tokens': 11, 'total_tokens': 40}

"""
