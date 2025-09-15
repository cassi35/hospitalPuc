from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoDeleteSpy(EnderecoRepositoryInterface):
    def __init__(self) -> None:
        self.delete_endereco_id = None
        self.delete_endereco_call_count = 0

    def delete_endereco(self, endereco_id: int) -> None:
        self.delete_endereco_id = endereco_id
        self.delete_endereco_call_count += 1
