from typing import Dict
from src.domain.models.exame_model import Exame

class ExameUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_exame_id = None
        self.update_exame_attributes = {}
        
    def update(self, exame_id: int, exame: Exame) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_exame_id = exame_id
        self.update_exame_attributes = exame.__dict__
        
        return {
            "type": "Exame",
            "count": 1,
            "attributes": {
                "id": exame_id,
                **self.update_exame_attributes
            }
        }
