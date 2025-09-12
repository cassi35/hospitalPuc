from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.prescricao import Prescricao

class PrescricaoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, prescricao: Prescricao) -> Dict:
        """Insert new prescricao usecase"""
        pass
