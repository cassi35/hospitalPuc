from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.exame.list_exame import ExameListUseCase as ExameListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class ExameListController(ControllerInterface):
    def __init__(self,usecase:ExameListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
