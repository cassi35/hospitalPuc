from typing import Dict

class ConvenioDeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_convenio_id = None

    def delete(self, convenio_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_convenio_id = convenio_id

        return {
            "type": "Convenio",
            "count": 1,
            "attributes": {
                "id": convenio_id
            }
        }
