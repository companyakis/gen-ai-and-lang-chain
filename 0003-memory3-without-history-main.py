from dotenv import load_dotenv 

from langchain_openai import ChatOpenAI 

from langchain_core.messages import HumanMessage, AIMessage 

load_dotenv() 

# https://platform.openai.com/docs/models

model = ChatOpenAI(model="gpt-4o-mini")

messages = [
    HumanMessage(content="Hi. How are you? My names is Gokboru!"),
    AIMessage(content="Hi Gokboru! How should I help you:)"),
    HumanMessage(content="Ok. What's my name?")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response.content) # Your name is Gokboru! How can I assist you today?

