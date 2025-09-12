from typing import Dict
from src.domain.usecases.exame.update_exame import ExameUpdateUseCase as ExameUpdateInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface 
from src.infra.db.entities.exame import Exame

class ExameUpdateUseCase(ExameUpdateInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository
    
    def update(self, exame_id: int, exame: Exame) -> Dict:
        pass
