from typing import Dict
from src.domain.models.especialidade_model import Especialidade

class EspecialidadeUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_especialidade_id = None
        self.update_especialidade_attributes = {}
        
    def update(self, especialidade_id: int, especialidade: Especialidade) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_especialidade_id = especialidade_id
        self.update_especialidade_attributes = especialidade.__dict__
        
        return {
            "type": "Especialidade",
            "count": 1,
            "attributes": {
                "id": especialidade_id,
                **self.update_especialidade_attributes
            }
        }
