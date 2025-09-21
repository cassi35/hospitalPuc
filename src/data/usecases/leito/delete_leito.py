from src.domain.usecases.leito.delete_leito import LeitoDeleteUseCase as LeitoDeleteInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface
from typing import Dict
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.validation_error import ValidationError
class LeitoDeleteUseCase(LeitoDeleteInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def delete(self, leito_id: int) -> Dict:
        self.__validate_leito_id(leito_id=leito_id)
        self.__delete_leito(leito_id=leito_id)
        response = self.__format_response(leito_id=leito_id)
        return response
    def __validate_leito_id(self,leito_id:int)-> None:
        if not isinstance(leito_id, int) or leito_id <= 0:
            raise ValidationError("O ID do leito deve ser um inteiro positivo.")
        leito = self.leito_repository.findById(id=leito_id)
        if not leito:
            raise HttpBadRequestError("Leito não encontrado para o ID fornecido.")
    def __delete_leito(self, leito_id: int) -> None:
        self.leito_repository.delete(id=leito_id)
    def __format_response(self,leito_id:int) -> Dict:
        response = {
            "type":"Leito",
            "count":1,
            "attributes":{
                "id":leito_id,
                "deleted":True
            }
        }
        return response