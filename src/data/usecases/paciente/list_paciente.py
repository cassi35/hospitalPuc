from typing import List, Dict
from src.domain.usecases.paciente.list_paciente import PacienteListUseCase as PacienteListInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface

class PacienteListUseCase(PacienteListInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository
    
    def list(self) -> List[Dict]:
        pass
