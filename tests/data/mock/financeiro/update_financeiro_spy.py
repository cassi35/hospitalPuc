from typing import Dict
from src.domain.models.financeiro_model import Financeiro

class FinanceiroUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_financeiro_id = None
        self.update_financeiro_attributes = {}
        
    def update(self, financeiro_id: int, financeiro: Financeiro) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_financeiro_id = financeiro_id
        self.update_financeiro_attributes = financeiro.__dict__
        
        return {
            "type": "Financeiro",
            "count": 1,
            "attributes": {
                "id": financeiro_id,
                **self.update_financeiro_attributes
            }
        }
