from abc import ABC, abstractmethod

class InternacaoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, internacao_id: int) -> None:
        """Delete internacao by id usecase"""
        pass
