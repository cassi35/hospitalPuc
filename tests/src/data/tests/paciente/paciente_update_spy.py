from typing import Dict
from src.infra.db.entities.paciente import Paciente
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteUpdateSpy(PacienteRepositoryInterface):
    def __init__(self) -> None:
        self.update_paciente_attributes = {}
        self.update_paciente_call_count = 0

    def update_paciente(self, paciente_id: int, paciente: Paciente) -> None:
        self.update_paciente_attributes = vars(paciente)
        self.update_paciente_attributes['id'] = paciente_id
        self.update_paciente_call_count += 1
