from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.setor_model import Setor

class SetorInsertUseCase(ABC):
    @abstractmethod
    def insert(self, setor: Setor) -> Dict:
        """Insert new setor usecase"""
        pass
