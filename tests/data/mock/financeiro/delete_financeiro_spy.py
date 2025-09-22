from typing import Dict

class FinanceiroDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_financeiro_id = None

    def delete(self, financeiro_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_financeiro_id = financeiro_id

        return {
            "type": "Financeiro",
            "count": 1,
            "attributes": {
                "id": financeiro_id
            }
        }
