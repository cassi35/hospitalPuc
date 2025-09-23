from typing import Dict
from src.domain.usecases.endereco.update_endereco import EnderecoUpdateUseCase as EnderecoUpdateInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface 
from src.domain.models.endereco_model import Endereco
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
class EnderecoUpdateUseCase(EnderecoUpdateInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def update(self, endereco_id: int, endereco: Endereco) -> Dict:
        self.__exists_endereco(id=endereco_id)
        self.validate_informations(endereco=endereco)
        self.endereco_repository.update_endereco(
        endereco_id,
        endereco.rua,
        endereco.bairro,
        endereco.cidade,
        endereco.estado,
        endereco.cep
        )
        return self.format_response(endereco=endereco)
    def __exists_endereco(self,id:int)-> None:
        endereco = self.endereco_repository.select_endereco(id=id)
        if not endereco:
            raise HttpNotFoundError("Endereço não encontrado")
        return None
    def validate_informations(self,endereco:Endereco) -> None:
        if not endereco.rua or endereco.rua.strip() == "":
            raise HttpBadRequestError("Rua inválida")
        if not endereco.bairro or endereco.bairro.strip() == "":
            raise HttpBadRequestError("Bairro inválido")
        if not endereco.cidade or endereco.cidade.strip() == "":
            raise HttpBadRequestError("Cidade inválida")
        if not endereco.estado or endereco.estado.strip() == "":
            raise HttpBadRequestError("Estado inválido")
        if not endereco.cep or endereco.cep.strip() == "" or len(endereco.cep) != 8 or not endereco.cep.isdigit():
            raise HttpBadRequestError("CEP inválido")
        if not self.endereco_repository.find_by_cep(endereco.cep):
            raise HttpNotFoundError("CEP não encontrado")
        return None

    def format_response(self,endereco:Endereco)-> Dict:
        response = {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                "id": endereco.id,
                "rua": endereco.rua,
                "bairro": endereco.bairro,
                "cidade": endereco.cidade,
                "estado": endereco.estado,
                "cep": endereco.cep
            }
        }
        return response