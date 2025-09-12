from abc import ABC, abstractmethod
from typing import List, Dict

class ConvenioListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all convenios usecase"""
        pass
