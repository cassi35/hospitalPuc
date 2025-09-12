from abc import ABC, abstractmethod

class LeitoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, leito_id: int) -> None:
        """Delete leito by id usecase"""
        pass
