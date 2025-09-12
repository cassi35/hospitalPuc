from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.internacao import Internacao

class InternacaoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, internacao: Internacao) -> Dict:
        """Insert new internacao usecase"""
        pass
