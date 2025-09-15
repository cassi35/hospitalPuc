from typing import Dict
from src.infra.db.entities.paciente import Paciente
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteInsertSpy(PacienteRepositoryInterface):
    def __init__(self) -> None:
        self.insert_paciente_attributes = {}
        self.insert_paciente_call_count = 0

    def insert_paciente(self, paciente: Paciente) -> None:
        self.insert_paciente_attributes = vars(paciente)
        self.insert_paciente_call_count += 1
