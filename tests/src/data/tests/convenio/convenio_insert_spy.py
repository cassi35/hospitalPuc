from typing import Dict
from src.infra.db.entities.convenio import Convenio
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioInsertSpy(ConvenioRepositoryInterface):
    def __init__(self) -> None:
        self.insert_convenio_attributes = {}
        self.insert_convenio_call_count = 0

    def insert_convenio(self, convenio: Convenio) -> None:
        self.insert_convenio_attributes = vars(convenio)
        self.insert_convenio_call_count += 1
