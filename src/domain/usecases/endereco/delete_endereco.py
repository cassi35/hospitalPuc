from abc import ABC, abstractmethod

class EnderecoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, endereco_id: int) -> dict:
        """Delete endereco by id usecase"""
        pass
