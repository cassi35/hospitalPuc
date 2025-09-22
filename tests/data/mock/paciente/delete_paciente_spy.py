from typing import Dict

class PacienteDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_paciente_id = None

    def delete(self, paciente_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_paciente_id = paciente_id

        return {
            "type": "Paciente",
            "count": 1,
            "attributes": {
                "id": paciente_id
            }
        }
