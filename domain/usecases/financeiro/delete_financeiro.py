from abc import ABC, abstractmethod

class FinanceiroDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, financeiro_id: int) -> None:
        """Delete financeiro by id usecase"""
        pass
