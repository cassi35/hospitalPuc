from typing import Dict
from src.domain.models.medico_model import Medico

class MedicoInsertUsecaseSpy:
    def __init__(self):
        self.insert_medico_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, medico: Medico) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_medico_attributes = medico.__dict__
        
        return {
            "type": "Medico",
            "count": 1,
            "attributes": {
                **self.insert_medico_attributes
            }
        }
