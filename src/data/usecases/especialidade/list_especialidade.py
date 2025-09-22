from typing import List, Dict
from src.domain.usecases.especialidade.list_especialidade import EspecialidadeListUseCase as EspecialidadeListInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from src.domain.models.especialidade_model import Especialidade
class EspecialidadeListUseCase(EspecialidadeListInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def list(self) -> List[Dict]:
        especialidades = self.especialidade_repository.findAll()
        return [self.format_response(especialidade) for especialidade in especialidades]
    def format_response(self,especialidade:Especialidade)-> Dict:
        return {
            "type":"Especialidade",
            "id": especialidade.id,
            "attributes":{
                "nome": especialidade.nome,
                "descricao": especialidade.descricao
            }
        }
