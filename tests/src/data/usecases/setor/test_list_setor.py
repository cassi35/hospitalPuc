from typing import List, Dict
from src.domain.usecases.setor.list_setor import SetorListUseCase as SetorListInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface

class SetorListUseCase(SetorListInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def list(self) -> List[Dict]:
        pass
