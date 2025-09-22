from typing import Dict
from src.domain.models.medicamento_model import Medicamento

class MedicamentoInsertUsecaseSpy:
    def __init__(self):
        self.insert_medicamento_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, medicamento: Medicamento) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_medicamento_attributes = medicamento.__dict__
        
        return {
            "type": "Medicamento",
            "count": 1,
            "attributes": {
                **self.insert_medicamento_attributes
            }
        }
