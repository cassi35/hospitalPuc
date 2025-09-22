from typing import Dict

class EspecialidadeDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_especialidade_id = None

    def delete(self, especialidade_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_especialidade_id = especialidade_id

        return {
            "type": "Especialidade",
            "count": 1,
            "attributes": {
                "id": especialidade_id
            }
        }
