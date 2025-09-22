from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.especialidade_model import Especialidade

class EspecialidadeUpdateUseCase(ABC):
    @abstractmethod
    def update(self, especialidade_id: int, especialidade: Especialidade) -> Dict:
        """Update existing especialidade usecase"""
        pass
