from abc import ABC, abstractmethod
from typing import List, Dict

class MedicoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all medicos usecase"""
        pass
