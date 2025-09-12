from typing import List, Dict
from src.domain.usecases.leito.list_leito import LeitoListUseCase as LeitoListInterface
from src.data.interfaces.leito_interface_repository import LeitoRepositoryInterface

class LeitoListUseCase(LeitoListInterface):
    def __init__(self, leito_repository: LeitoRepositoryInterface):
        self.leito_repository = leito_repository
    
    def list(self) -> List[Dict]:
        pass
