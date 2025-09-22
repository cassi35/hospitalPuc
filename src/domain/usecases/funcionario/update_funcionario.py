from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.funcionario_model import Funcionario

class FuncionarioUpdateUseCase(ABC):
    @abstractmethod
    def update(self, funcionario_id: int, funcionario: Funcionario) -> Dict:
        """Update existing funcionario usecase"""
        pass
