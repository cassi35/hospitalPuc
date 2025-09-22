from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.exame_model import Exame

class ExameInsertUseCase(ABC):
    @abstractmethod
    def insert(self, exame: Exame) -> Dict:
        """Insert new exame usecase"""
        pass
