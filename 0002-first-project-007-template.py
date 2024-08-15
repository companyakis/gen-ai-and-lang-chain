from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage

# there are a lot of parsers!

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4",
    temperature=0.15
)

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Please, translate the following into {language}"),

        ("user", "{text}")
    ]
)

parser = StrOutputParser()

chain = prompt_template | model | parser


if __name__ == "__main__":
    print(chain.invoke({"language": "french", "text" : "hello"}))


