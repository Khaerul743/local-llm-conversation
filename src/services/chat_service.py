from collections.abc import Iterator
from uuid import uuid4

from langchain_core.messages import HumanMessage

from src.llm.agent import Agent


class ChatService:
    def __init__(self):
        self._agent = Agent()

    def _get_config(self, conversation_id: str) -> dict:
        return {
            "configurable": {
                "thread_id": conversation_id,
            }
        }

    def create_conversation(self) -> str:
        return str(uuid4())

    def send_message(
        self,
        conversation_id: str,
        message: str,
    ) -> str:

        response = self._agent.get_agent().invoke(
            {"messages": [HumanMessage(content=message)]},
            config=self._get_config(conversation_id),
        )

        return response["messages"][-1].content

    def stream_message(
        self,
        conversation_id: str,
        message: str,
    ) -> Iterator[str]:

        agent = self._agent.get_agent()

        for chunk, metadata in agent.stream(
            {"messages": [HumanMessage(content=message)]},
            config=self._get_config(conversation_id),
            stream_mode="messages",
        ):
            # Hanya mengambil output dari model node
            if metadata.get("langgraph_node") != "model":
                continue

            content = chunk.content

            if isinstance(content, str) and content:
                yield content

    def get_history(
        self,
        conversation_id: str,
    ) -> list:

        state = self._agent.get_agent().get_state(
            config=self._get_config(conversation_id)
        )

        if not state.values:
            return []

        return state.values.get("messages", [])

    def clear_conversation(
        self,
        conversation_id: str,
    ) -> None:

        agent = self._agent.get_agent()

        agent.update_state(
            config=self._get_config(conversation_id),
            values={"messages": []},
        )
