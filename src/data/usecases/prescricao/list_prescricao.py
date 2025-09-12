from typing import List, Dict
from src.domain.usecases.prescricao.list_prescricao import PrescricaoListUseCase as PrescricaoListInterface
from src.data.interfaces.prescricao_interface_repository import PrescricaoRepositoryInterface

class PrescricaoListUseCase(PrescricaoListInterface):
    def __init__(self, prescricao_repository: PrescricaoRepositoryInterface):
        self.prescricao_repository = prescricao_repository
    
    def list(self) -> List[Dict]:
        pass
