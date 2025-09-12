from abc import ABC, abstractmethod

class MedicamentoDeleteUseCase(ABC):
    @abstractmethod
    def delete(self, medicamento_id: int) -> None:
        """Delete medicamento by id usecase"""
        pass
