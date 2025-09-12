from abc import ABC, abstractmethod
from typing import List, Dict

class FuncionarioListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all funcionarios usecase"""
        pass
