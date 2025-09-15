from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface

class MedicamentoDeleteSpy(MedicamentoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_medicamento_id = None
        self.delete_medicamento_call_count = 0

    def delete_medicamento(self, medicamento_id: int) -> None:
        self.delete_medicamento_id = medicamento_id
        self.delete_medicamento_call_count += 1
