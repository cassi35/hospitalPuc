from typing import List, Dict
from src.domain.usecases.medico.list_medico import MedicoListUseCase as MedicoListInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface

class MedicoListUseCase(MedicoListInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def list(self) -> List[Dict]:
        pass
