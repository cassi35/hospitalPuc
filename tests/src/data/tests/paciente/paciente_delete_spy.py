from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteDeleteSpy(PacienteRepositoryInterface):
    def __init__(self) -> None:
        self.delete_paciente_id = None
        self.delete_paciente_call_count = 0

    def delete_paciente(self, paciente_id: int) -> None:
        self.delete_paciente_id = paciente_id
        self.delete_paciente_call_count += 1
