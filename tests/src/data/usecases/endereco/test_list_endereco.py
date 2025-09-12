from typing import List, Dict
from src.domain.usecases.endereco.list_endereco import EnderecoListUseCase as EnderecoListInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface

class EnderecoListUseCase(EnderecoListInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def list(self) -> List[Dict]:
        pass
