from src.llm import LLMClient
from langchain.messages import SystemMessage, HumanMessage

client = LLMClient()

llm = client.get_llm()

messages = [
    SystemMessage(content="you are helpful assistant"),
    HumanMessage(content="Hai")
]
print(llm.invoke(messages))