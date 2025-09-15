from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface

class ExameDeleteSpy(ExameRepositoryInterface):
    def __init__(self) -> None:
        self.delete_exame_id = None
        self.delete_exame_call_count = 0

    def delete_exame(self, exame_id: int) -> None:
        self.delete_exame_id = exame_id
        self.delete_exame_call_count += 1
