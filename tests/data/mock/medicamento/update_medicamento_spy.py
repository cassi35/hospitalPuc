from typing import Dict
from src.domain.models.medicamento_model import Medicamento

class MedicamentoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_medicamento_id = None
        self.update_medicamento_attributes = {}
        
    def update(self, medicamento_id: int, medicamento: Medicamento) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_medicamento_id = medicamento_id
        self.update_medicamento_attributes = medicamento.__dict__
        
        return {
            "type": "Medicamento",
            "count": 1,
            "attributes": {
                "id": medicamento_id,
                **self.update_medicamento_attributes
            }
        }
