from abc import ABC, abstractmethod

class ConvenioDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, convenio_id: int) -> None:
        """Delete convenio by id usecase"""
        pass
