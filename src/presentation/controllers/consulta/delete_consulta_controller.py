from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.consulta.delete_consulta import ConsultaDeleteUseCase as ConsultaDeleteInterface
class ConsultaDeleteController(ControllerInterface): 
    def __init__(self,usecase:ConsultaDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        consulta_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            consulta_id=consulta_id
        )
        return HTTPResponse(status_code=200,body=response)
