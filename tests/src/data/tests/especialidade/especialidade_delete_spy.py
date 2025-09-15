from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface

class EspecialidadeDeleteSpy(EspecialidadeRepositoryInterface):
    def __init__(self) -> None:
        self.delete_especialidade_id = None
        self.delete_especialidade_call_count = 0

    def delete_especialidade(self, especialidade_id: int) -> None:
        self.delete_especialidade_id = especialidade_id
        self.delete_especialidade_call_count += 1
