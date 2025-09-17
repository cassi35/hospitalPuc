from src.domain.usecases.setor.delete_setor import SetorDeleteUseCase as SetorDeleteInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from typing import Dict
from src.errors.types.validation_error import ValidationError
class SetorDeleteUseCase(SetorDeleteInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def delete(self, setor_id: int) -> Dict:
        self.__validate_setor_id(setor_id=setor_id)
        self.__setor_exists(id=setor_id)
        self.__delete_setor(id=setor_id)
        response = self.__format_response(id=setor_id)
        return response
    def __validate_setor_id(self,setor_id:int)-> None:
        if not isinstance(setor_id,int) or setor_id <= 0:
            raise ValidationError("ID do setor deve ser um inteiro positivo")
    def __setor_exists(self,id:int)-> None:
        setor = self.setor_repository.findById(id=id)
        if not setor:
            raise ValidationError("Setor não encontrado")
    def __delete_setor(self,id:int)-> None:
        self.setor_repository.delete(id=id)
        return None
    def __format_response(self,id:int)-> Dict:
        response = {
            "type":"Setor",
            "count":1,
            "attributes":{
                "id":id,
                "deleted":True
            }
        }
        return response