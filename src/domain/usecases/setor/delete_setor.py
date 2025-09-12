from abc import ABC, abstractmethod

class SetorDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, setor_id: int) -> None:
        """Delete setor by id usecase"""
        pass
