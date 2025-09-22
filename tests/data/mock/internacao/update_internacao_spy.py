from typing import Dict
from src.domain.models.internacao_model import Internacao

class InternacaoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_internacao_id = None
        self.update_internacao_attributes = {}
        
    def update(self, internacao_id: int, internacao: Internacao) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_internacao_id = internacao_id
        self.update_internacao_attributes = internacao.__dict__
        
        return {
            "type": "Internacao",
            "count": 1,
            "attributes": {
                "id": internacao_id,
                **self.update_internacao_attributes
            }
        }
