from langchain_core.messages import HumanMessage, SystemMessage

from src.llm.agent import Agent

agent = Agent()
messages = [
    SystemMessage(content="You are helpful assistant"),
    HumanMessage(content="Apa itu filsafat berdasarkan dokument"),
]
