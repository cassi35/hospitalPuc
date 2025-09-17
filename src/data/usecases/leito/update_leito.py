from typing import Dict
from src.domain.usecases.leito.update_leito import LeitoUpdateUseCase as LeitoUpdateInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface 
from src.infra.db.entities.leito import Leito
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
class LeitoUpdateUseCase(LeitoUpdateInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface, setor_repository: SetorRepositoryInterface):
        self.leito_repository = leito_repository
        self.setor_repository = setor_repository
    def update(self, leito_id: int, leito: Leito) -> Dict:
        self.__leito_exists(id=leito_id)
        self.__validate_informations(leito=leito)
        self.__update_leito(id=leito_id,leito=leito)
        response = self.__format_response(leito=leito)
        return response
    def __leito_exists(self,id:int)->None:
        leito = self.leito_repository.findById(id=id)
        if not leito:
            raise HttpNotFoundError("Leito não encontrado")
        return None
    def __validate_informations(self,leito:Leito)-> None:
        if leito.numero_leito < 0 or leito.numero_leito > 30:
            raise HttpBadRequestError("Número do leito inválido. Deve estar entre 0 e 30.")
        setor = self.setor_repository.findById(id=leito.setor_id)
        if not setor:
            raise HttpBadRequestError("Setor não encontrado para o ID fornecido.")
        if leito.tipo not in ['Enfermaria', 'Apartamento', 'UTI Adulto', 'UTI Neonatal', 'UTI Pediátrica']:
            raise HttpBadRequestError("tipo de leito invalido")
        if leito.status not in ['disponivel','ocupado']:
            raise HttpBadRequestError("status do leito invalido")
        return None
    def __update_leito(self,id:int,leito:Leito)-> None:
        self.leito_repository.update(
            id=id,
            numero_leito=leito.numero_leito,
            setor_id=leito.setor_id,
            tipo=leito.tipo,
            status=leito.status
        )
    def __format_response(self,leito:Leito)-> Dict:
        response = {
            "type":"Leito",
            "id":leito.id,
            "attributes":{
                "numero_leito":leito.numero_leito,
                "setor_id":leito.setor_id,
                "tipo":leito.tipo,
                "status":leito.status
            }
        }
        return response
