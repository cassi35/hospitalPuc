from typing import List, Dict
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioListSpy(ConvenioRepositoryInterface):
    def __init__(self) -> None:
        self.list_convenio_call_count = 0
        self.list_convenio_return = []

    def list_convenio(self) -> List[Dict]:
        self.list_convenio_call_count += 1
        return self.list_convenio_return
