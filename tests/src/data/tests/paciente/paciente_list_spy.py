from typing import List, Dict
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteListSpy(PacienteRepositoryInterface):
    def __init__(self) -> None:
        self.list_paciente_call_count = 0
        self.list_paciente_return = []

    def list_paciente(self) -> List[Dict]:
        self.list_paciente_call_count += 1
        return self.list_paciente_return
