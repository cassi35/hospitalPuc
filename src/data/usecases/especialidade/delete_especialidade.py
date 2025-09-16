from src.domain.usecases.especialidade.delete_especialidade import EspecialidadeDeleteUseCase as EspecialidadeDeleteInterface
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface
from typing import Dict
class EspecialidadeDeleteUseCase(EspecialidadeDeleteInterface):
    def __init__(self, especialidade_repository: EspecialidadeRepositoryInterface):
        self.especialidade_repository = especialidade_repository
    
    def delete(self, especialidade_id: int) -> Dict:
        pass
