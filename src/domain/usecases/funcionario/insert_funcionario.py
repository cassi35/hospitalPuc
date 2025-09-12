from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.funcionario import Funcionario

class FuncionarioInsertUseCase(ABC):
    @abstractmethod
    def insert(self, funcionario: Funcionario) -> Dict:
        """Insert new funcionario usecase"""
        pass
