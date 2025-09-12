from abc import ABC, abstractmethod
from typing import List, Dict

class LeitoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all leitos usecase"""
        pass
