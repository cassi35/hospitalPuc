from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.internacao_model import Internacao

class InternacaoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, internacao: Internacao) -> Dict:
        """Insert new internacao usecase"""
        pass
