# ...existing code...
from typing import List, Dict
from src.domain.usecases.consulta.list_consulta import ConsultaListUseCase as ConsultaListInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface
from src.domain.models.consulta_model import Consulta

class ConsultaListUseCase(ConsultaListInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository

    def list(self) -> List[Dict]:
        consultas = self.consulta_repository.findAll()
        return [self.__format_response(consulta) for consulta in consultas]

    def __format_response(self, consulta: Consulta) -> Dict:
        response = {
            "type": "Consulta",
            "id": getattr(consulta, "id", None),
            "attributes": {
                "data_hora": getattr(consulta, "data_hora", None),
                "paciente_id": getattr(consulta, "paciente_id", None),
                "medico_id": getattr(consulta, "medico_id", None),
                "especialidade_id": getattr(consulta, "especialidade_id", None),
                "status": getattr(consulta, "status", None),
                "observacoes": getattr(consulta, "observacoes", None)
            }
        }
        return response