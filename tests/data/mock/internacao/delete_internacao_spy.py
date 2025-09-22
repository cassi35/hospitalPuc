from typing import Dict

class InternacaoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_internacao_id = None

    def delete(self, internacao_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_internacao_id = internacao_id

        return {
            "type": "Internacao",
            "count": 1,
            "attributes": {
                "id": internacao_id
            }
        }
