from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.consulta import Consulta

class ConsultaInsertUseCase(ABC):
    @abstractmethod
    def insert(self, consulta: Consulta) -> Dict:
        """Insert new consulta usecase"""
        pass
