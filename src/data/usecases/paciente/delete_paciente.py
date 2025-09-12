from src.domain.usecases.paciente.delete_paciente import PacienteDeleteUseCase as PacienteDeleteInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteDeleteUseCase(PacienteDeleteInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def delete(self, paciente_id: int) -> None:
        pass
