from typing import Dict
from src.domain.usecases.convenio.update_convenio import ConvenioUpdateUseCase as ConvenioUpdateInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface 
from src.domain.models.convenio_model import Convenio
from src.errors.types.validation_error import ValidationError
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
class ConvenioUpdateUseCase(ConvenioUpdateInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def update(self, convenio_id: int, convenio: Convenio) -> Dict:
        self.__validate_id(convenio_id=convenio_id)
        self.__validate_informations(nome=convenio.nome,tipo_plano= convenio.tipo_plano)
        self.__update_convenio(convenio_id=convenio.id,nome=convenio.nome,tipo_plano=convenio.tipo_plano)
        response = self.__format_response(nome=convenio.nome,tipo_plano=convenio.tipo_plano)
        return response
    def __validate_id(self, convenio_id: int) -> None:
        if not isinstance(convenio_id, int):
            raise ValidationError("ID deve ser um inteiro")
        if convenio_id <= 0:
            raise ValidationError("ID deve ser um inteiro positivo")
        return None
    def __validate_informations(self, nome: str, tipo_plano: str) -> None:
        if len(nome) < 1 or len(nome) > 30:
            raise ValidationError("Falta de caracteres")
        if tipo_plano not in ['Individual', 'Familiar', 'Empresarial']:
            raise ValidationError("Tipo de plano inválido")
        if not nome.isalpha():
            raise HttpBadRequestError("Somente caracteres")
        if not tipo_plano.isalpha():
            raise HttpBadRequestError("Somente caracteres")
        return  None
    def __update_convenio(self, convenio_id: int, nome: str, tipo_plano: str) -> None:
        convenio = self.convenio_repository.select_convenio(id=convenio_id)
        if not convenio:

            raise HttpNotFoundError("convenio nao achado")
        self.convenio_repository.udpate_convenio(id=convenio_id,nome=nome,tipo_plano=tipo_plano)
        return None
    def __format_response(self, nome: str, tipo_plano: str) -> Dict:
        response = {
            "type": "Convenio",
            "count": 1,
            "attributes": {
                "nome": nome,
                "tipo_plano": tipo_plano
            }
        }
        return response

