from typing import Dict
from src.domain.models.exame_model import Exame

class ExameInsertUsecaseSpy:
    def __init__(self):
        self.insert_exame_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, exame: Exame) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_exame_attributes = exame.__dict__
        
        return {
            "type": "Exame",
            "count": 1,
            "attributes": {
                **self.insert_exame_attributes
            }
        }
