from typing import List, Dict
from src.domain.usecases.endereco.list_endereco import EnderecoListUseCase as EnderecoListInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from src.infra.db.entities.endereco import  Endereco
class EnderecoListUseCase(EnderecoListInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def list(self) -> List[Dict]:
        enderecos = self.endereco_repository.select_all_enderecos()
        return [self.format_response(endereco) for endereco in enderecos]

    def format_response(self, endereco: Endereco) -> Dict:
        return {
            "type": "Endereco",
            "id": endereco.id,
            "attributes": {
                "rua": endereco.rua,
                "bairro": endereco.bairro,
                "cidade": endereco.cidade,
                "estado": endereco.estado,
                "cep": endereco.cep
            }
        }
