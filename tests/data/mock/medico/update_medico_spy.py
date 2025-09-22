from typing import Dict
from src.domain.models.medico_model import Medico

class MedicoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_medico_id = None
        self.update_medico_attributes = {}
        
    def update(self, medico_id: int, medico: Medico) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_medico_id = medico_id
        self.update_medico_attributes = medico.__dict__
        
        return {
            "type": "Medico",
            "count": 1,
            "attributes": {
                "id": medico_id,
                **self.update_medico_attributes
            }
        }
