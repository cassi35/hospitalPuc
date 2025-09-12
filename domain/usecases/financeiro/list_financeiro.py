from abc import ABC, abstractmethod
from typing import List, Dict

class FinanceiroListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all financeiros usecase"""
        pass
