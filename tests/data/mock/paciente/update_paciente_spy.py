from typing import Dict
from src.domain.models.paciente_model import Paciente

class PacienteUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_paciente_id = None
        self.update_paciente_attributes = {}
        
    def update(self, paciente_id: int, paciente: Paciente) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_paciente_id = paciente_id
        self.update_paciente_attributes = paciente.__dict__
        
        return {
            "type": "Paciente",
            "count": 1,
            "attributes": {
                "id": paciente_id,
                **self.update_paciente_attributes
            }
        }
