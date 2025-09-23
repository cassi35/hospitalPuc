from typing import Dict, List
from src.domain.usecases.endereco.insert_endereco import EnderecoInsertUseCase as EnderecoInsertInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface 
from src.domain.models.endereco_model import Endereco
from src.errors.types.http_bad_request import HttpBadRequestError

class EnderecoInsertUseCase(EnderecoInsertInterface):
    def __init__(self, endereco_repository: EnderecoRepositoryInterface):
        self.endereco_repository = endereco_repository
    
    def insert(self, endereco: Endereco) -> Dict:
        self._validate_informations(
            rua=endereco.rua,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
            estado=endereco.estado,
            cep=endereco.cep
        )
        self._insert_endereco(
            rua=endereco.rua,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
            estado=endereco.estado,
            cep=endereco.cep
        )
        response = self._format_response(
            rua=endereco.rua,
            bairro=endereco.bairro,
            cidade=endereco.cidade,
            estado=endereco.estado,
            cep=endereco.cep
        )
        return response

    def _validate_informations(self, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        if len(rua) > 30 or len(rua) < 1:
            raise HttpBadRequestError("rua: falta de caracteres")
        if len(bairro) > 30 or len(bairro) < 1:
            raise HttpBadRequestError("bairro: falta de caracteres")
        if len(cidade) > 30 or len(cidade) < 1:
            raise HttpBadRequestError("cidade: falta de caracteres")
        if len(estado) > 30 or len(estado) < 1:
            raise HttpBadRequestError("estado: falta de caracteres")
        elif not estado.replace(" ", "").isalpha():  # Remove espaços para validar
            raise HttpBadRequestError("estado deve conter somente caracteres")
        if len(cep) != 8 or not cep.isdigit():
            raise HttpBadRequestError("cep invalido") 

    def _insert_endereco(self, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> None:
        self.endereco_repository.insert_endereco(
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            estado=estado,
            cep=cep,
        )

    def _format_response(self, rua: str, bairro: str, cidade: str, estado: str, cep: str) -> Dict:
        response = {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                "rua": rua,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
        }
        return response