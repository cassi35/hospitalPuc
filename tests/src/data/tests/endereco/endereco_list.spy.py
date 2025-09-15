from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoListSpy(EnderecoRepositoryInterface):
    def __init__(self) -> None:
        self.list_endereco_call_count = 0
        self.list_endereco_return = []

    def list_endereco(self):
        self.list_endereco_call_count += 1
        return self.list_endereco_return