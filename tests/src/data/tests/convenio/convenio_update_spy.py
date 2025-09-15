from typing import Dict
from src.infra.db.entities.convenio import Convenio
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface

class ConvenioUpdateSpy(ConvenioRepositoryInterface):
    def __init__(self) -> None:
        self.update_convenio_attributes = {}
        self.update_convenio_call_count = 0

    def update_convenio(self, convenio_id: int, convenio: Convenio) -> None:
        self.update_convenio_attributes = vars(convenio)
        self.update_convenio_attributes['id'] = convenio_id
        self.update_convenio_call_count += 1
