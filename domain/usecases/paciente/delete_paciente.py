from abc import ABC, abstractmethod

class PacienteDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, paciente_id: int) -> None:
        """Delete paciente by id usecase"""
        pass
