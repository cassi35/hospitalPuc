from typing import List, Dict
from src.domain.usecases.setor.list_setor import SetorListUseCase as SetorListInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from src.domain.models.setor_model import Setor
class SetorListUseCase(SetorListInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def list(self) -> List[Dict]:
        setores = self.setor_repository.findAll()
        return [self.__list_format_response(setor) for setor in setores]
    def __list_format_response(self,setor:Setor)-> Dict:
        response = {
            "type":"Setor",
            "id":setor.id,
            "attributes":{
                "nome":setor.nome,
                "andar":setor.andar,
                "capacidade":setor.capacidade,
                "responsavel":setor.responsavel
            }
        }
        return response