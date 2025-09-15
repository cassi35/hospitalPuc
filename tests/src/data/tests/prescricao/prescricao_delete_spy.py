from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface

class PrescricaoDeleteSpy(PrescricaoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_prescricao_id = None
        self.delete_prescricao_call_count = 0

    def delete_prescricao(self, prescricao_id: int) -> None:
        self.delete_prescricao_id = prescricao_id
        self.delete_prescricao_call_count += 1
