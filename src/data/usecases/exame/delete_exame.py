from src.domain.usecases.exame.delete_exame import ExameDeleteUseCase as ExameDeleteInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from typing import Dict

class ExameDeleteUseCase(ExameDeleteInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository
    
    def delete(self, exame_id: int) -> Dict:
        pass
