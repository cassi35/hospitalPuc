from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.paciente_model import Paciente

class PacienteInsertUseCase(ABC):
    @abstractmethod
    def insert(self, paciente: Paciente) -> Dict:
        """Insert new paciente usecase"""
        pass
