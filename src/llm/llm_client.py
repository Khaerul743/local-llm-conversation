from langchain_ollama import ChatOllama
from langchain.chat_models import BaseChatModel
from src.config.settings import settings
from langchain_openai import ChatOpenAI

class LLMClient:
    def __init__(self):
        self.llm_mode = settings.LLM_MODE
        self.llm_model = settings.LLM_MODEL

    def get_llm(self) -> BaseChatModel:
        if self.llm_mode == "local":
            llm = ChatOllama(model=settings.LLM_MODEL, temperature=0.7)
            return llm

        return ChatOpenAI(model=settings.LLM_MODEL, temperature=0.7)

