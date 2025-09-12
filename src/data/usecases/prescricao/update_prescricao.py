from typing import Dict
from src.domain.usecases.prescricao.update_prescricao import PrescricaoUpdateUseCase as PrescricaoUpdateInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface 
from src.infra.db.entities.prescricao import Prescricao

class PrescricaoUpdateUseCase(PrescricaoUpdateInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository
    
    def update(self, prescricao_id: int, prescricao: Prescricao) -> Dict:
        pass
