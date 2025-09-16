from src.domain.usecases.medicamento.delete_medicamento import MedicamentoDeleteUseCase as MedicamentoDeleteInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from typing import Dict

class MedicamentoDeleteUseCase(MedicamentoDeleteInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository
    
    def delete(self, medicamento_id: int) -> Dict:
        pass
