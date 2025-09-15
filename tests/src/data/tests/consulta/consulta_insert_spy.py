from typing import Dict
from src.infra.db.entities.consulta import Consulta
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaInsertSpy(ConsultaRepositoryInterface):
    def __init__(self) -> None:
        self.insert_consulta_attributes = {}
        self.insert_consulta_call_count = 0

    def insert_consulta(self, consulta: Consulta) -> None:
        self.insert_consulta_attributes = vars(consulta)
        self.insert_consulta_call_count += 1
