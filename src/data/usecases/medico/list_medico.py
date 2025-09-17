from typing import List, Dict
from src.domain.usecases.medico.list_medico import MedicoListUseCase as MedicoListInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.infra.db.entities.medico import Medico
class MedicoListUseCase(MedicoListInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository

    def list(self) -> List[Dict]:
        medicos = self.medico_repository.findAll()
        return [self.__list_format_response(medico) for medico in medicos] 
    def __list_format_response(self,medico:Medico) -> Dict:
        response = {
            "type":"Medico",
            "id":medico.id,
            "attributes":{
                "nome":medico.nome,
                "cpf":medico.cpf,
                "especialidade_id":medico.especialidade_id,
                "telefone":medico.telefone,
                "email":medico.email,
                "status":medico.status
            }
        }
        return response
