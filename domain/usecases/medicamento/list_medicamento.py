from abc import ABC, abstractmethod
from typing import List, Dict

class MedicamentoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all medicamentos usecase"""
        pass
