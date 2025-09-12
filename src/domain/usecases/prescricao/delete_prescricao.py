from abc import ABC, abstractmethod

class PrescricaoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, prescricao_id: int) -> None:
        """Delete prescricao by id usecase"""
        pass
