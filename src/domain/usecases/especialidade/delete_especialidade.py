from abc import ABC, abstractmethod

class EspecialidadeDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, especialidade_id: int) -> None:
        """Delete especialidade by id usecase"""
        pass
