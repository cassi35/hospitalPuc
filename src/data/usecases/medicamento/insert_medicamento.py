from typing import Dict
from src.domain.usecases.medicamento.insert_medicamento import MedicamentoInsertUseCase as MedicamentoInsertInterface
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface 
from src.infra.db.entities.medicamento import Medicamento

class MedicamentoInsertUseCase(MedicamentoInsertInterface):
    def __init__(self, medicamento_repository: MedicamentoRepositoryInterface):
        self.medicamento_repository = medicamento_repository
    
    def insert(self, medicamento: Medicamento) -> Dict:
        pass
