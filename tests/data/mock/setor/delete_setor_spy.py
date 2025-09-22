from typing import Dict

class SetorDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_setor_id = None

    def delete(self, setor_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_setor_id = setor_id

        return {
            "type": "Setor",
            "count": 1,
            "attributes": {
                "id": setor_id
            }
        }
