from dotenv import load_dotenv 

from langchain_openai import ChatOpenAI 

from langchain_core.messages import HumanMessage

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv() 

# https://platform.openai.com/docs/models

model = ChatOpenAI(model="gpt-4o-mini")

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You're now my assistant. Please, answer all the questions in a smart way."),
        MessagesPlaceholder(variable_name = "messages")
    ]
)

chain = prompt | model

config = {"configurable": {"session_id": "chat-001"}}

with_message_history = RunnableWithMessageHistory(chain, get_session_history)

situation: bool = True

if __name__ == "__main__":
    
    while situation:
        user_input = input("Your message: ")
        response = with_message_history.invoke(
            [HumanMessage(content = user_input)],
            config = config
        )
        
        print(response.content)

# Your message: Hi my name is Mustafa Buyukdereli. Can I ask some questions?
# Hi Mustafa! Of course, feel free to ask any questions you have, and I'll do my best to help you.
