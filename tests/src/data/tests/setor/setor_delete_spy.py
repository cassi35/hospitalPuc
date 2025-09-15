from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorDeleteSpy(SetorRepositoryInterface):
    def __init__(self) -> None:
        self.delete_setor_id = None
        self.delete_setor_call_count = 0

    def delete_setor(self, setor_id: int) -> None:
        self.delete_setor_id = setor_id
        self.delete_setor_call_count += 1
