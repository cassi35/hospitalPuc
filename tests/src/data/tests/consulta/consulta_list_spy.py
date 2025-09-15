from typing import List, Dict
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaListSpy(ConsultaRepositoryInterface):
    def __init__(self) -> None:
        self.list_consulta_call_count = 0
        self.list_consulta_return = []

    def list_consulta(self) -> List[Dict]:
        self.list_consulta_call_count += 1
        return self.list_consulta_return
