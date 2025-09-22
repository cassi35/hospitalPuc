from typing import Dict
from src.domain.models.leito_model import Leito

class LeitoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_leito_id = None
        self.update_leito_attributes = {}
        
    def update(self, leito_id: int, leito: Leito) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_leito_id = leito_id
        self.update_leito_attributes = leito.__dict__
        
        return {
            "type": "Leito",
            "count": 1,
            "attributes": {
                "id": leito_id,
                **self.update_leito_attributes
            }
        }
