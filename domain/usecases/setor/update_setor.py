from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.setor import Setor

class SetorUpdateUseCase(ABC):
    @abstractmethod
    def update(self, setor_id: int, setor: Setor) -> Dict:
        """Update existing setor usecase"""
        pass
