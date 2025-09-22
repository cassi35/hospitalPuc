from typing import Dict
from src.domain.models.paciente_model import Paciente

class PacienteInsertUsecaseSpy:
    def __init__(self):
        self.insert_paciente_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, paciente: Paciente) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_paciente_attributes = paciente.__dict__
        
        return {
            "type": "Paciente",
            "count": 1,
            "attributes": {
                **self.insert_paciente_attributes
            }
        }
