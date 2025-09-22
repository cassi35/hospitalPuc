from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.prescricao_model import Prescricao

class PrescricaoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, prescricao_id: int, prescricao: Prescricao) -> Dict:
        """Update existing prescricao usecase"""
        pass
