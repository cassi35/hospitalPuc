from typing import Dict

class MedicamentoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_medicamento_id = None

    def delete(self, medicamento_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_medicamento_id = medicamento_id

        return {
            "type": "Medicamento",
            "count": 1,
            "attributes": {
                "id": medicamento_id
            }
        }
