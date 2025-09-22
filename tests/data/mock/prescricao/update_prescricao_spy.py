from typing import Dict
from src.domain.models.prescricao_model import Prescricao

class PrescricaoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_prescricao_id = None
        self.update_prescricao_attributes = {}
        
    def update(self, prescricao_id: int, prescricao: Prescricao) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_prescricao_id = prescricao_id
        self.update_prescricao_attributes = prescricao.__dict__
        
        return {
            "type": "Prescricao",
            "count": 1,
            "attributes": {
                "id": prescricao_id,
                **self.update_prescricao_attributes
            }
        }
