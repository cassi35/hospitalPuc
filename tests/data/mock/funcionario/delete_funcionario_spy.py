from typing import Dict

class FuncionarioDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_funcionario_id = None

    def delete(self, funcionario_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_funcionario_id = funcionario_id

        return {
            "type": "Funcionario",
            "count": 1,
            "attributes": {
                "id": funcionario_id
            }
        }
