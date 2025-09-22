from typing import Dict
from src.domain.models.funcionario_model import Funcionario

class FuncionarioUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_funcionario_id = None
        self.update_funcionario_attributes = {}
        
    def update(self, funcionario_id: int, funcionario: Funcionario) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_funcionario_id = funcionario_id
        self.update_funcionario_attributes = funcionario.__dict__
        
        return {
            "type": "Funcionario",
            "count": 1,
            "attributes": {
                "id": funcionario_id,
                **self.update_funcionario_attributes
            }
        }
