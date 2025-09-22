from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.consulta.update_consulta import ConsultaUpdateUseCase as ConsultaUpdateInterface
from src.domain.models.consulta_model import Consulta as ConsultaDomain
class ConsultaUpdateController(ControllerInterface):
    def __init__(self,usecase:ConsultaUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        consulta_id = int(http_request.path_params["id"])
        consulta = ConsultaDomain(**http_request.body) 
        consulta.id = consulta_id
        response = self.usecase.update(
            consulta_id=consulta_id,
            consulta=consulta
        )
        return HTTPResponse(status_code=200,body=response)
