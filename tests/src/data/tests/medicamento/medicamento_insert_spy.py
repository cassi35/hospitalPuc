from typing import Dict
from src.infra.db.entities.medicamento import Medicamento
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface

class MedicamentoInsertSpy(MedicamentoRepositoryInterface):
    def __init__(self) -> None:
        self.insert_medicamento_attributes = {}
        self.insert_medicamento_call_count = 0

    def insert_medicamento(self, medicamento: Medicamento) -> None:
        self.insert_medicamento_attributes = vars(medicamento)
        self.insert_medicamento_call_count += 1
