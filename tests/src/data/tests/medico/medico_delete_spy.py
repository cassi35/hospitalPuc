from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoDeleteSpy(MedicoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_medico_id = None
        self.delete_medico_call_count = 0

    def delete_medico(self, medico_id: int) -> None:
        self.delete_medico_id = medico_id
        self.delete_medico_call_count += 1
