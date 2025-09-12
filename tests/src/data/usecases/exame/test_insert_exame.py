from typing import Dict
from src.domain.usecases.exame.insert_exame import ExameInsertUseCase as ExameInsertInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface 
from src.infra.db.entities.exame import Exame

class ExameInsertUseCase(ExameInsertInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository
    
    def insert(self, exame: Exame) -> Dict:
        pass
