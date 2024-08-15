from langchain_openai import ChatOpenAI

# there are a lot of parsers!

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate

from fastapi import FastAPI

from langserve import add_routes

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

# FastAPI and route part!

app = FastAPI(
    title="Let's Use LangChain Server",
    version="0.0.1",
    description="FastAPI and LangChain"
)

add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=5000)

# http://localhost:5000/chain/playground


