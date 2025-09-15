from typing import Dict
from src.infra.db.entities.consulta import Consulta
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaUpdateSpy(ConsultaRepositoryInterface):
    def __init__(self) -> None:
        self.update_consulta_attributes = {}
        self.update_consulta_call_count = 0

    def update_consulta(self, consulta_id: int, consulta: Consulta) -> None:
        self.update_consulta_attributes = vars(consulta)
        self.update_consulta_attributes['id'] = consulta_id
        self.update_consulta_call_count += 1
