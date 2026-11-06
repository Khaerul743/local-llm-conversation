from uuid import uuid4
from typing import Iterator

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, BaseMessage
from src.llm import LLMClient


class ChatService:
    def __init__(self):
        self._llm_client = LLMClient()
        self._llm = self._llm_client.get_llm()
        self._system_prompt = (
            "You are a helpful AI assistant. "
            "Answer questions clearly, accurately, "
            "and concisely."
        )

        self.conversations = dict[str, list[BaseMessage]] = {}

    def create_conversation(self) -> str:
        conversation_id: str = str(uuid4())

        self.conversations[self.conversation_id] = [
            SystemMessage(content=self._system_prompt)
        ]

        return conversation_id

    def get_history(self, conversation_id: str) -> list[BaseMessage]:
        if conversation_id not in self.conversations:
            raise ValueError("Conversation not found")
        return self.conversations[conversation_id]

    def _update_history(self, conversation_id: str, new_conversation_history: list[BaseMessage]) -> None:
        if conversation_id not in self.conversations:
            raise ValueError("Conversation not found")
        self.conversations[conversation_id] = new_conversation_history
        return
    
    def send_message(self, conversation_id: str, message: str) -> str:
        history = self.get_history(conversation_id)
        history.append(HumanMessage(content=message))

        response = self._llm.invoke(history)
        history.append(response)

        self._update_history(conversation_id, history)

        return response.content

    def stream_message(
        self,
        conversation_id: str,
        message: str,
    ) -> Iterator[str]:

        history = self.get_history(conversation_id)

        history.append(
            HumanMessage(content=message)
        )

        response_chunks = []

        for chunk in self.llm.stream(history):
            content = chunk.content

            if isinstance(content, str) and content:
                response_chunks.append(content)
                yield content

        # Save complete AI response after streaming
        full_response = "".join(response_chunks)

        history.append(
            AIMessage(content=full_response)
        )

    def clear_conversation(
        self,
        conversation_id: str,
    ) -> None:

        if conversation_id not in self.conversations:
            raise ValueError("Conversation not found.")

        self.conversations[conversation_id] = [
            SystemMessage(content=self.system_prompt)
        ]