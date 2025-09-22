from typing import Dict
from src.domain.models.consulta_model import Consulta

class ConsultaUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_consulta_id = None
        self.update_consulta_attributes = {}
        
    def update(self, consulta_id: int, consulta: Consulta) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_consulta_id = consulta_id
        self.update_consulta_attributes = consulta.__dict__
        
        return {
            "type": "Consulta",
            "count": 1,
            "attributes": {
                "id": consulta_id,
                **self.update_consulta_attributes
            }
        }
