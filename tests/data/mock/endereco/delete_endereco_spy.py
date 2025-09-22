from typing import Dict

class EnderecoDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_endereco_id = None

    def delete(self, endereco_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_endereco_id = endereco_id

        return {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                "id": endereco_id
            }
        }
