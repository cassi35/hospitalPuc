from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.exame_model import Exame

class ExameUpdateUseCase(ABC):
    @abstractmethod
    def update(self, exame_id: int, exame: Exame) -> Dict:
        """Update existing exame usecase"""
        pass
