from abc import ABC, abstractmethod

class MedicoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, medico_id: int) -> None:
        """Delete medico by id usecase"""
        pass
