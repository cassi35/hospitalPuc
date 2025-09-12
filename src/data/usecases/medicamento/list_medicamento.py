from typing import List, Dict
from src.domain.usecases.medicamento.list_medicamento import MedicamentoListUseCase as MedicamentoListInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface

class MedicamentoListUseCase(MedicamentoListInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository
    
    def list(self) -> List[Dict]:
        pass
