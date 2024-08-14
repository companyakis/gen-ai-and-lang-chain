from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage

# there are a lot of parsers!

from langchain_core.output_parsers import StrOutputParser

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

parser = StrOutputParser()

result = model.invoke(messages)

if __name__ == "__main__":
    print(parser.invoke(result))
