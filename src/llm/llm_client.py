import ollama
from langchain_ollama import ChatOllama
from langchain_core.language_models.chat_models import BaseChatModel
from src.config.settings import settings
from langchain_openai import ChatOpenAI

class LLMClient:
    def __init__(self):
        self.llm_mode = settings.LLM_MODE
        self.llm_model = settings.LLM_MODEL
        self._client = ollama.Client(host=settings.OLLAMA_HOST)

    def _check_connection(self) -> bool:
        try:
            models = self._client.list()
            available_models = [model.model for model in models.models]
            return self.llm_model in available_models
        except Exception:
            return False
        
    def get_llm(self) -> BaseChatModel:
        if self.llm_mode == "local":
            if not self._check_connection():
                raise ConnectionError("Ollama connection error or model not found.")
            
            llm = ChatOllama(model=settings.LLM_MODEL, temperature=settings.LLM_TEMPERATURE)
            return llm

        return ChatOpenAI(model=settings.LLM_MODEL, temperature=settings.LLM_TEMPERATURE)

