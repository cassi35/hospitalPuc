from typing import Dict

class LeitoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_leito_id = None

    def delete(self, leito_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_leito_id = leito_id

        return {
            "type": "Leito",
            "count": 1,
            "attributes": {
                "id": leito_id
            }
        }
