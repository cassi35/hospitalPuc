from typing import Dict
from src.domain.usecases.paciente.insert_paciente import PacienteInsertUseCase as PacienteInsertInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface 
from src.infra.db.entities.paciente import Paciente

class PacienteInsertUseCase(PacienteInsertInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def insert(self, paciente: Paciente) -> Dict:
        pass
