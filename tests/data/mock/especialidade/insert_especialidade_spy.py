from typing import Dict
from src.domain.models.especialidade_model import Especialidade

class EspecialidadeInsertUsecaseSpy:
    def __init__(self):
        self.insert_especialidade_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, especialidade: Especialidade) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_especialidade_attributes = especialidade.__dict__
        
        return {
            "type": "Especialidade",
            "count": 1,
            "attributes": {
                **self.insert_especialidade_attributes
            }
        }
