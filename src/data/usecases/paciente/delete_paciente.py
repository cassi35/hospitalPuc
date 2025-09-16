from src.domain.usecases.paciente.delete_paciente import PacienteDeleteUseCase as PacienteDeleteInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from typing import Dict
from errors.types.http_not_found import HttpNotFoundError
class PacienteDeleteUseCase(PacienteDeleteInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def delete(self, paciente_id: int) -> Dict:
         self.__validate_paciente_id(paciente_id=paciente_id)
         self.__validate_paciente_exists(id=paciente_id)
         self.__delete_paciente(paciente_id=paciente_id)
         response = self.__format_response(paciente_id=paciente_id)
         return response
    def __validate_paciente_id(self,paciente_id:int)-> None:
        if not isinstance(paciente_id,int) or paciente_id <= 0:
            raise HttpNotFoundError("ID do paciente deve ser um numero positivo")
        return None
    def __validate_paciente_exists(self,id:int)-> None:
        paciente = self.paciente_repository.select_paciente(id=id)
        if not paciente:
            raise HttpNotFoundError("paciente nao existe mais")
        return None
    def __delete_paciente(self,paciente_id:int)-> None:
        self.paciente_repository.delete_paciente(id=paciente_id)
        return None
    def __format_response(self, paciente_id: int) -> Dict:
        response = {
            "type":"Paciente",
            "count":1,
            "attributes":{
                "id": paciente_id,
                "deleted": True
            }
        }
        return response 