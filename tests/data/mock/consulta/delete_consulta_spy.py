from typing import Dict

class ConsultaDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_consulta_id = None

    def delete(self, consulta_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_consulta_id = consulta_id

        return {
            "type": "Consulta",
            "count": 1,
            "attributes": {
                "id": consulta_id
            }
        }
