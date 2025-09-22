from typing import Dict
from src.domain.models.setor_model import Setor

class SetorInsertUsecaseSpy:
    def __init__(self):
        self.insert_setor_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, setor: Setor) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_setor_attributes = setor.__dict__
        
        return {
            "type": "Setor",
            "count": 1,
            "attributes": {
                **self.insert_setor_attributes
            }
        }
