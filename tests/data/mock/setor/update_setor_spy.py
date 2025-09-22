from typing import Dict
from src.domain.models.setor_model import Setor

class SetorUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_setor_id = None
        self.update_setor_attributes = {}
        
    def update(self, setor_id: int, setor: Setor) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_setor_id = setor_id
        self.update_setor_attributes = setor.__dict__
        
        return {
            "type": "Setor",
            "count": 1,
            "attributes": {
                "id": setor_id,
                **self.update_setor_attributes
            }
        }
