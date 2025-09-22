from typing import Dict
from src.domain.models.prescricao_model import Prescricao

class PrescricaoInsertUsecaseSpy:
    def __init__(self):
        self.insert_prescricao_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, prescricao: Prescricao) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_prescricao_attributes = prescricao.__dict__
        
        return {
            "type": "Prescricao",
            "count": 1,
            "attributes": {
                **self.insert_prescricao_attributes
            }
        }
