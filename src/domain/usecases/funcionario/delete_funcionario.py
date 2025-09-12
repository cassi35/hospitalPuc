from abc import ABC, abstractmethod

class FuncionarioDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, funcionario_id: int) -> None:
        """Delete funcionario by id usecase"""
        pass
