from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.exame import Exame

class ExameUpdateUseCase(ABC):
    @abstractmethod
    def update(self, exame_id: int, exame: Exame) -> Dict:
        """Update existing exame usecase"""
        pass
