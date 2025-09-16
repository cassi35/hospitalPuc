from src.domain.usecases.especialidade.delete_especialidade import EspecialidadeDeleteUseCase as EspecialidadeDeleteInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from typing import Dict
from src.errors.types.http_bad_request import HttpBadRequestError
class EspecialidadeDeleteUseCase(EspecialidadeDeleteInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def delete(self, especialidade_id: int) -> Dict:
        self.__validate_informations(especialidade_id=especialidade_id)
        self.__delete_especialidade(especialidade_id=especialidade_id)
        response = self.__format_response(especialidade_id=especialidade_id)
        return response
    def __validate_informations(self,especialidade_id:int)-> None:
        if not especialidade_id or especialidade_id <= 0:
            raise HttpBadRequestError("id invalido")
        if not self.especialidade_repository.findById(id=especialidade_id):
            raise HttpBadRequestError("especialidade nao encontrada")
        return None
    def __delete_especialidade(self,especialidade_id:int) -> None:
        self.especialidade_repository.delete(id=especialidade_id)
        return None
    def __format_response(self,especialidade_id:int) -> Dict:
        response = {
            "type":"Especialidade",
            "count":1,
            "attributes":{
                "id": especialidade_id
            }
        } 
        return response