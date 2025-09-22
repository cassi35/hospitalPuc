from typing import Dict
from src.domain.models.endereco_model import Endereco

class EnderecoInsertUsecaseSpy:
    def __init__(self):
        self.insert_endereco_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, endereco: Endereco) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_endereco_attributes = endereco.__dict__
        
        return {
            "type": "Endereco",
            "count": 1,
            "attributes": {
                **self.insert_endereco_attributes
            }
        }
