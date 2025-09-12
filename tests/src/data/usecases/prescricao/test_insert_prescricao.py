from typing import Dict
from src.domain.usecases.prescricao.insert_prescricao import PrescricaoInsertUseCase as PrescricaoInsertInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface 
from src.infra.db.entities.prescricao import Prescricao

class PrescricaoInsertUseCase(PrescricaoInsertInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository
    
    def insert(self, prescricao: Prescricao) -> Dict:
        pass
