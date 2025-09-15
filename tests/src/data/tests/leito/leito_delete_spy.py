from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoDeleteSpy(LeitoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_leito_id = None
        self.delete_leito_call_count = 0

    def delete_leito(self, leito_id: int) -> None:
        self.delete_leito_id = leito_id
        self.delete_leito_call_count += 1
