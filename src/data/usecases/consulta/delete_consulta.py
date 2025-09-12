from src.domain.usecases.consulta.delete_consulta import ConsultaDeleteUseCase as ConsultaDeleteInterface
from src.data.interfaces.consulta_interface_repository import ConsultaRepositoryInterface

class ConsultaDeleteUseCase(ConsultaDeleteInterface):
    def __init__(self, consulta_repository: ConsultaRepositoryInterface):
        self.consulta_repository = consulta_repository
    
    def delete(self, consulta_id: int) -> None:
        pass
