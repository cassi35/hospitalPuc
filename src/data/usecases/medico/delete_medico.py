from src.domain.usecases.medico.delete_medico import MedicoDeleteUseCase as MedicoDeleteInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from typing import Dict
from src.errors.types.http_not_found import HttpNotFoundError
from src.errors.types.http_bad_request import HttpBadRequestError
class MedicoDeleteUseCase(MedicoDeleteInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def delete(self, medico_id: int) -> Dict:
        self.__validate_medico_id(medico_id=medico_id)
        self.__exists_medico(medico_id=medico_id)
        self.__delete_medico(medico_id=medico_id)
        response = self.__format_response(medico_id=medico_id)
        return response
    def __validate_medico_id(self,medico_id:int) -> None:
        if not isinstance(medico_id,int) or medico_id <= 0:
            raise HttpBadRequestError("ID do medico deve ser um numero positivo")
        return None
    def __exists_medico(self,medico_id:int) -> None:
        medico = self.medico_repository.findById(id=medico_id)
        if not medico:
            raise HttpNotFoundError("Medico não encontrado")
        return None 
    def __delete_medico(self,medico_id:int) -> None:
        self.medico_repository.delete(id=medico_id)
        return None
    def __format_response(self,medico_id:int)-> Dict:
        response = {
            "type":"Medico",
            "count":1,
            "attributes":{
                "id":medico_id,
                "deleted":True
            }
        }
        return response