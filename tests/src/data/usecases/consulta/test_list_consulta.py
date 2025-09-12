from typing import List, Dict
from src.domain.usecases.consulta.list_consulta import ConsultaListUseCase as ConsultaListInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaListUseCase(ConsultaListInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository
    
    def list(self) -> List[Dict]:
        pass
