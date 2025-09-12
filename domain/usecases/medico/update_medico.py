from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.medico import Medico

class MedicoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, medico_id: int, medico: Medico) -> Dict:
        """Update existing medico usecase"""
        pass
