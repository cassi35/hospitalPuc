from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.convenio_model import Convenio

class ConvenioInsertUseCase(ABC):
    @abstractmethod
    def insert(self, convenio: Convenio) -> Dict:
        """Insert new convenio usecase"""
        pass
