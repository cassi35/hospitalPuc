from typing import List, Dict
from src.domain.usecases.especialidade.list_especialidade import EspecialidadeListUseCase as EspecialidadeListInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface

class EspecialidadeListUseCase(EspecialidadeListInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def list(self) -> List[Dict]:
        pass
