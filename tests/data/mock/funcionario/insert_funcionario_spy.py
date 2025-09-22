from typing import Dict
from src.domain.models.funcionario_model import Funcionario

class FuncionarioInsertUsecaseSpy:
    def __init__(self):
        self.insert_funcionario_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, funcionario: Funcionario) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_funcionario_attributes = funcionario.__dict__
        
        return {
            "type": "Funcionario",
            "count": 1,
            "attributes": {
                **self.insert_funcionario_attributes
            }
        }
