from typing import Dict
from src.domain.usecases.leito.update_leito import LeitoUpdateUseCase as LeitoUpdateInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface 
from src.infra.db.entities.leito import Leito

class LeitoUpdateUseCase(LeitoUpdateInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def update(self, leito_id: int, leito: Leito) -> Dict:
        pass
