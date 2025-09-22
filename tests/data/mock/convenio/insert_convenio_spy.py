from typing import Dict
from src.domain.models.convenio_model import Convenio

class ConvenioInsertUsecaseSpy:
    def __init__(self):
        self.insert_convenio_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, convenio: Convenio) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_convenio_attributes = convenio.__dict__
        
        return {
            "type": "Convenio",
            "count": 1,
            "attributes": {
                **self.insert_convenio_attributes
            }
        }
