from typing import Dict
from src.domain.models.convenio_model import Convenio

class ConvenioUpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_convenio_id = None
        self.update_convenio_attributes = {}
        
    def update(self, convenio_id: int, convenio: Convenio) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_convenio_id = convenio_id
        self.update_convenio_attributes = convenio.__dict__
        
        return {
            "type": "Convenio",
            "count": 1,
            "attributes": {
                "id": convenio_id,
                **self.update_convenio_attributes
            }
        }
