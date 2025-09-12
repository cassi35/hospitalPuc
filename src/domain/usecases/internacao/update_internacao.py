from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.internacao import Internacao

class InternacaoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, internacao_id: int, internacao: Internacao) -> Dict:
        """Update existing internacao usecase"""
        pass
