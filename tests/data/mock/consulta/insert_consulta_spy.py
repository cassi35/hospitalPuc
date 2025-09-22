from typing import Dict
from src.domain.models.consulta_model import Consulta

class ConsultaInsertUsecaseSpy:
    def __init__(self):
        self.insert_consulta_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, consulta: Consulta) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_consulta_attributes = consulta.__dict__
        
        return {
            "type": "Consulta",
            "count": 1,
            "attributes": {
                **self.insert_consulta_attributes
            }
        }
