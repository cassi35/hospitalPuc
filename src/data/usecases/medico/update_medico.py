from typing import Dict
from src.domain.usecases.medico.update_medico import MedicoUpdateUseCase as MedicoUpdateInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface 
from src.infra.db.entities.medico import Medico

class MedicoUpdateUseCase(MedicoUpdateInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def update(self, medico_id: int, medico: Medico) -> Dict:
        pass
