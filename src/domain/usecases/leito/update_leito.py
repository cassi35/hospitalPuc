from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.leito_model import Leito

class LeitoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, leito_id: int, leito: Leito) -> Dict:
        """Update existing leito usecase"""
        pass
