from typing import Dict
from src.domain.usecases.especialidade.update_especialidade import EspecialidadeUpdateUseCase as EspecialidadeUpdateInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface 
from src.infra.db.entities.especialidade import Especialidade

class EspecialidadeUpdateUseCase(EspecialidadeUpdateInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def update(self, especialidade_id: int, especialidade: Especialidade) -> Dict:
        pass
