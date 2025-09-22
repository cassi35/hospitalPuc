from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.leito_model import Leito

class LeitoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, leito: Leito) -> Dict:
        """Insert new leito usecase"""
        pass
