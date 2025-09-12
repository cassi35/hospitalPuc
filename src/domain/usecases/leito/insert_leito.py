from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.leito import Leito

class LeitoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, leito: Leito) -> Dict:
        """Insert new leito usecase"""
        pass
