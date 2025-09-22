from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.medico_model import Medico

class MedicoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, medico: Medico) -> Dict:
        """Insert new medico usecase"""
        pass
