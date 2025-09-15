from src.data.interfaces.internacao_interface_repository import InternacaoRepositoryInterface

class InternacaoDeleteSpy(InternacaoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_internacao_id = None
        self.delete_internacao_call_count = 0

    def delete_internacao(self, internacao_id: int) -> None:
        self.delete_internacao_id = internacao_id
        self.delete_internacao_call_count += 1
