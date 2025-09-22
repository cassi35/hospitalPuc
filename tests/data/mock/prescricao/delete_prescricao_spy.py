from typing import Dict

class PrescricaoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_prescricao_id = None

    def delete(self, prescricao_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_prescricao_id = prescricao_id

        return {
            "type": "Prescricao",
            "count": 1,
            "attributes": {
                "id": prescricao_id
            }
        }
