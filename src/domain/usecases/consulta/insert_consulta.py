from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.consulta_model import Consulta

class ConsultaInsertUseCase(ABC):
    @abstractmethod
    def insert(self, consulta: Consulta) -> Dict:
        """Insert new consulta usecase"""
        pass
