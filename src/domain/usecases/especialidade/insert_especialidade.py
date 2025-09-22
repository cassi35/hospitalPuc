from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.especialidade_model import Especialidade

class EspecialidadeInsertUseCase(ABC):
    @abstractmethod
    def insert(self, especialidade: Especialidade) -> Dict:
        """Insert new especialidade usecase"""
        pass
