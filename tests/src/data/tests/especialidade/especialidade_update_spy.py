from typing import Dict
from src.infra.db.entities.especialidade import Especialidade
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface

class EspecialidadeUpdateSpy(EspecialidadeRepositoryInterface):
    def __init__(self) -> None:
        self.update_especialidade_attributes = {}
        self.update_especialidade_call_count = 0

    def update_especialidade(self, especialidade_id: int, especialidade: Especialidade) -> None:
        self.update_especialidade_attributes = vars(especialidade)
        self.update_especialidade_attributes['id'] = especialidade_id
        self.update_especialidade_call_count += 1
