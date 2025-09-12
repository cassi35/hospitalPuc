from typing import Dict, List
from src.domain.usecases.endereco.insert_endereco import EnderecoInsertUseCase as EnderecoInsertInterface
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface 
from src.infra.db.entities.endereco import Endereco
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
        informations: List[str] = [rua, bairro, cidade, estado, cep]
        for idx, value in enumerate(informations):
            if idx == 4:  # CEP
                if len(value) != 8 or not value.isdigit():
                    raise HttpBadRequestError("cep invalido")
            elif len(value) > 30 or len(value) < 1:
                raise HttpBadRequestError("falta de caracteres")
            elif not value.isalpha():
                raise HttpBadRequestError("somente caracteres")

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