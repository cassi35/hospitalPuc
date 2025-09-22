from typing import Dict
from src.domain.models.leito_model import Leito

class LeitoInsertUsecaseSpy:
    def __init__(self):
        self.insert_leito_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, leito: Leito) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_leito_attributes = leito.__dict__
        
        return {
            "type": "Leito",
            "count": 1,
            "attributes": {
                **self.insert_leito_attributes
            }
        }
