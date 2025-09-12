from abc import ABC, abstractmethod
from typing import List, Dict

class SetorListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all setors usecase"""
        pass
