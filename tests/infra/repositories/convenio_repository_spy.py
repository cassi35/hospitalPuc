from typing import List, Optional
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.infra.db.entities.convenio import Convenio
class ConvenioRepositorySpy(ConvenioRepositoryInterface):
    def __init__(self):
        self.insert_convenio_attributes = {}
        self.insert_convenio_call_count = 0
        
        self.delete_convenio_attributes = {}
        self.delete_convenio_call_count = 0

        self.select_convenio_attributes = {}
        self.select_convenio_call_count = 0 

        self.udpate_convenio_attributes = {}
        self.udpate_convenio_call_count = 0 

        self.delete_convenio_return = True
        
