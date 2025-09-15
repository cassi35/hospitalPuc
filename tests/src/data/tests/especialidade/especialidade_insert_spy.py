from typing import Dict
from src.infra.db.entities.especialidade import Especialidade
from src.data.interfaces.especialidade_interface_repository import EspecialidadeRepositoryInterface

class EspecialidadeInsertSpy(EspecialidadeRepositoryInterface):
    def __init__(self) -> None:
        self.insert_especialidade_attributes = {}
        self.insert_especialidade_call_count = 0

    def insert_especialidade(self, especialidade: Especialidade) -> None:
        self.insert_especialidade_attributes = vars(especialidade)
        self.insert_especialidade_call_count += 1
