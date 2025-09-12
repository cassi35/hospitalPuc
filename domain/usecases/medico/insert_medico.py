from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.medico import Medico

class MedicoInsertUseCase(ABC):
    @abstractmethod
    def insert(self, medico: Medico) -> Dict:
        """Insert new medico usecase"""
        pass
