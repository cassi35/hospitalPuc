from typing import Dict

class MedicoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_medico_id = None

    def delete(self, medico_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_medico_id = medico_id

        return {
            "type": "Medico",
            "count": 1,
            "attributes": {
                "id": medico_id
            }
        }
