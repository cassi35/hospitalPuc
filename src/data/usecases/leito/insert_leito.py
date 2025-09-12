from typing import Dict
from src.domain.usecases.leito.insert_leito import LeitoInsertUseCase as LeitoInsertInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface 
from src.infra.db.entities.leito import Leito

class LeitoInsertUseCase(LeitoInsertInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def insert(self, leito: Leito) -> Dict:
        pass
