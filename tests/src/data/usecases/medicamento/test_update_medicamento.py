from typing import Dict
from src.domain.usecases.medicamento.update_medicamento import MedicamentoUpdateUseCase as MedicamentoUpdateInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface 
from src.infra.db.entities.medicamento import Medicamento

class MedicamentoUpdateUseCase(MedicamentoUpdateInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository
    
    def update(self, medicamento_id: int, medicamento: Medicamento) -> Dict:
        pass
