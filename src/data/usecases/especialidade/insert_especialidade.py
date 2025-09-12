from typing import Dict
from src.domain.usecases.especialidade.insert_especialidade import EspecialidadeInsertUseCase as EspecialidadeInsertInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface 
from src.infra.db.entities.especialidade import Especialidade

class EspecialidadeInsertUseCase(EspecialidadeInsertInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def insert(self, especialidade: Especialidade) -> Dict:
        pass
