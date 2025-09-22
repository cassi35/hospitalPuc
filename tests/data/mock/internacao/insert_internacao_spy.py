from typing import Dict
from src.domain.models.internacao_model import Internacao

class InternacaoInsertUsecaseSpy:
    def __init__(self):
        self.insert_internacao_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, internacao: Internacao) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_internacao_attributes = internacao.__dict__
        
        return {
            "type": "Internacao",
            "count": 1,
            "attributes": {
                **self.insert_internacao_attributes
            }
        }
