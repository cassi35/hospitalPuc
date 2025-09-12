from typing import Dict
from src.domain.usecases.endereco.update_endereco import EnderecoUpdateUseCase as EnderecoUpdateInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface 
from src.infra.db.entities.endereco import Endereco

class EnderecoUpdateUseCase(EnderecoUpdateInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def update(self, endereco_id: int, endereco: Endereco) -> Dict:
        pass
