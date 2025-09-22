from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.paciente.list_paciente import PacienteListUseCase as PacienteListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class PacienteListController(ControllerInterface):
    def __init__(self,usecase:PacienteListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
