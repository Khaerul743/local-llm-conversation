from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from src.llm.llm_client import LLMClient
from src.llm.tools import retrieve_document


class Agent:
    def __init__(self):
        self._llm_client = LLMClient()
        self._llm = self._llm_client.get_llm()
        self._checkpoint = InMemorySaver()

        self.agent = create_agent(
            model=self._llm, tools=[retrieve_document], checkpointer=self._checkpoint
        )

    def get_agent(self):
        return self.agent
