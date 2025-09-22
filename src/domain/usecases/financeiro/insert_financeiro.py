from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.financeiro_model import Financeiro

class FinanceiroInsertUseCase(ABC):
    @abstractmethod
    def insert(self, financeiro: Financeiro) -> Dict:
        """Insert new financeiro usecase"""
        pass
