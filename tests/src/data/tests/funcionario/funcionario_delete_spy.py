from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface

class FuncionarioDeleteSpy(FuncionarioRepositoryInterface):
    def __init__(self) -> None:
        self.delete_funcionario_id = None
        self.delete_funcionario_call_count = 0

    def delete_funcionario(self, funcionario_id: int) -> None:
        self.delete_funcionario_id = funcionario_id
        self.delete_funcionario_call_count += 1
