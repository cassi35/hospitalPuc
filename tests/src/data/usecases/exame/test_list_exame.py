from typing import List, Dict
from src.domain.usecases.exame.list_exame import ExameListUseCase as ExameListInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface

class ExameListUseCase(ExameListInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository
    
    def list(self) -> List[Dict]:
        pass
