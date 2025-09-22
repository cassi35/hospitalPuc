from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.funcionario.list_funcionario import FuncionarioListUseCase as FuncionarioListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class FuncionarioListController(ControllerInterface):
    def __init__(self,usecase:FuncionarioListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
