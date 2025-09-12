from typing import Dict
from src.domain.usecases.setor.insert_setor import SetorInsertUseCase as SetorInsertInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface 
from src.infra.db.entities.setor import Setor

class SetorInsertUseCase(SetorInsertInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def insert(self, setor: Setor) -> Dict:
        pass
