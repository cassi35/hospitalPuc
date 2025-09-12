from abc import ABC, abstractmethod
from typing import List, Dict

class EnderecoListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all enderecos usecase"""
        pass
