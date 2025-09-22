from typing import Dict
from src.domain.models.endereco_model import Endereco
class EnderecoInsertUsecaseSpy:
    def __init__(self):
        self.insert_endereco_attributes = {}
    def insert(self, endereco: Endereco) -> Dict:
        self.insert_endereco_attributes = endereco.__dict__
        return {
            "type":"endereco",
            "count": 1,
            "attributes":self.insert_endereco_attributes
        }