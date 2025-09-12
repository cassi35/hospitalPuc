from typing import Dict
from src.domain.usecases.setor.update_setor import SetorUpdateUseCase as SetorUpdateInterface
from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface 
from src.infra.db.entities.setor import Setor

class SetorUpdateUseCase(SetorUpdateInterface):
    def __init__(self, setor_repository: SetorRepositoryInterface):
        self.setor_repository = setor_repository
    
    def update(self, setor_id: int, setor: Setor) -> Dict:
        pass
