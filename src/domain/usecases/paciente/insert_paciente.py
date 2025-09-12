from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.paciente import Paciente

class PacienteInsertUseCase(ABC):
    @abstractmethod
    def insert(self, paciente: Paciente) -> Dict:
        """Insert new paciente usecase"""
        pass
