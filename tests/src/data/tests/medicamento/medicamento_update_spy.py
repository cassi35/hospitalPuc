from typing import Dict
from src.infra.db.entities.medicamento import Medicamento
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface

class MedicamentoUpdateSpy(MedicamentoRepositoryInterface):
    def __init__(self) -> None:
        self.update_medicamento_attributes = {}
        self.update_medicamento_call_count = 0

    def update_medicamento(self, medicamento_id: int, medicamento: Medicamento) -> None:
        self.update_medicamento_attributes = vars(medicamento)
        self.update_medicamento_attributes['id'] = medicamento_id
        self.update_medicamento_call_count += 1
