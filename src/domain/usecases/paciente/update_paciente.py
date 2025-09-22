from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.paciente_model import Paciente

class PacienteUpdateUseCase(ABC):
    @abstractmethod
    def update(self, paciente_id: int, paciente: Paciente) -> Dict:
        """Update existing paciente usecase"""
        pass
