from typing import Dict
from src.domain.usecases.paciente.update_paciente import PacienteUpdateUseCase as PacienteUpdateInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface 
from src.infra.db.entities.paciente import Paciente

class PacienteUpdateUseCase(PacienteUpdateInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def update(self, paciente_id: int, paciente: Paciente) -> Dict:
        pass
