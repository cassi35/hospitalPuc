from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.financeiro_model import Financeiro

class FinanceiroUpdateUseCase(ABC):
    @abstractmethod
    def update(self, financeiro_id: int, financeiro: Financeiro) -> Dict:
        """Update existing financeiro usecase"""
        pass
