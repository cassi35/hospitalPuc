from abc import ABC, abstractmethod
from typing import List, Dict

class ExameListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all exames usecase"""
        pass
