from typing import Dict
from src.domain.usecases.convenio.insert_convenio import ConvenioInsertUseCase as ConvenioInsertInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface 
from src.domain.models.convenio_model import Convenio
from src.errors.types.http_bad_request import HttpBadRequestError
class ConvenioInsertUseCase(ConvenioInsertInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def insert(self, convenio: Convenio) -> Dict:
        self.__validate_informations(nome=convenio.nome,tipo_plano=convenio.tipo_plano)
        self.__insert_convenio(nome=convenio.nome,tipo_plano=convenio.tipo_plano)
        response = self.__format_response(nome=convenio.nome,tipo_plano=convenio.tipo_plano)
        return response
    def __validate_informations(self, nome: str, tipo_plano: str) -> None:
        if(len(nome) < 1 or len(nome)>30):
            raise HttpBadRequestError("falta de caracteres")
        if(tipo_plano not in ['Individual','Familiar','Empresarial']):
            raise HttpBadRequestError("tipo de plano invalido")
        if (not nome.isalpha()):
            raise HttpBadRequestError("somente caracteres")
        if (not tipo_plano.isalpha()):
            raise HttpBadRequestError("somente caracteres")
        return None
    def __insert_convenio(self, nome: str, tipo_plano: str) -> None:
        self.convenio_repository.insert_convenio(tipo_plano=tipo_plano,nome=nome)
        return None

    def __format_response(self, nome: str, tipo_plano: str) -> Dict:
        response = {
            "type":"Convenio",
            "count":1,
            "attributes":{
                "nome":nome,
                "tipo_plano":tipo_plano
            }
        }
        return response