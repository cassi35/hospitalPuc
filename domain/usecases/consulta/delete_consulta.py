from abc import ABC, abstractmethod

class ConsultaDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, consulta_id: int) -> None:
        """Delete consulta by id usecase"""
        pass
