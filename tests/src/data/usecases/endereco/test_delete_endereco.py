from src.domain.usecases.endereco.delete_endereco import EnderecoDeleteUseCase as EnderecoDeleteInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoDeleteUseCase(EnderecoDeleteInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def delete(self, endereco_id: int) -> None:
        pass
