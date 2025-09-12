from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.funcionario import Funcionario

class FuncionarioUpdateUseCase(ABC):
    @abstractmethod
    def update(self, funcionario_id: int, funcionario: Funcionario) -> Dict:
        """Update existing funcionario usecase"""
        pass
