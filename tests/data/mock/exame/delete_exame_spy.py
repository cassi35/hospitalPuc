from typing import Dict

class ExameDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_exame_id = None

    def delete(self, exame_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_exame_id = exame_id

        return {
            "type": "Exame",
            "count": 1,
            "attributes": {
                "id": exame_id
            }
        }
