from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.especialidade import Especialidade

class EspecialidadeInsertUseCase(ABC):
    @abstractmethod
    def insert(self, especialidade: Especialidade) -> Dict:
        """Insert new especialidade usecase"""
        pass
