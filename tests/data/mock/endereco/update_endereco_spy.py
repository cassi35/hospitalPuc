from typing import Dict
from src.domain.models.endereco_model import Endereco

class EnderecoUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_endereco_id = None
        self.update_endereco_attributes = {}
        
    def update(self, endereco_id: int, endereco: Endereco) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_endereco_id = endereco_id
        self.update_endereco_attributes = endereco.__dict__
        
        return {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                "id": endereco_id,
                **self.update_endereco_attributes
            }
        }
