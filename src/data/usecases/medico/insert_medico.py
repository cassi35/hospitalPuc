from typing import Dict
from src.domain.usecases.medico.insert_medico import MedicoInsertUseCase as MedicoInsertInterface
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface 
from src.infra.db.entities.medico import Medico

class MedicoInsertUseCase(MedicoInsertInterface):
    def __init__(self, medico_repository: MedicoRepositoryInterface):
        self.medico_repository = medico_repository
    
    def insert(self, medico: Medico) -> Dict:
        pass
