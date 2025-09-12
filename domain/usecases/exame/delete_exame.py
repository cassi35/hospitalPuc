from abc import ABC, abstractmethod

class ExameDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, exame_id: int) -> None:
        """Delete exame by id usecase"""
        pass
