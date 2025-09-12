from abc import ABC, abstractmethod
from typing import List, Dict

class InternacaoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all internacaos usecase"""
        pass
