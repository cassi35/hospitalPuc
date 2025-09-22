from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.medicamento_model import Medicamento

class MedicamentoUpdateUseCase(ABC):
    @abstractmethod
    def update(self, medicamento_id: int, medicamento: Medicamento) -> Dict:
        """Update existing medicamento usecase"""
        pass
