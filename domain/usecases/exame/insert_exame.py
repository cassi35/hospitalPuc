from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.exame import Exame

class ExameInsertUseCase(ABC):
    @abstractmethod
    def insert(self, exame: Exame) -> Dict:
        """Insert new exame usecase"""
        pass
