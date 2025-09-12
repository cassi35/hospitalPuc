from abc import ABC, abstractmethod
from typing import List, Dict

class PrescricaoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all prescricaos usecase"""
        pass
