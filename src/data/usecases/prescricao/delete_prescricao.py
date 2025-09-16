from src.domain.usecases.prescricao.delete_prescricao import PrescricaoDeleteUseCase as PrescricaoDeleteInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface
from typing import Dict

class PrescricaoDeleteUseCase(PrescricaoDeleteInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository
    
    def delete(self, prescricao_id: int) -> Dict:
        pass
