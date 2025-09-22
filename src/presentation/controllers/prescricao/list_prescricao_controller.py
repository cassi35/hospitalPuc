from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.prescricao.list_prescricao import PrescricaoListUseCase as PrescricaoListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class PrescricaoListController(ControllerInterface):
    def __init__(self,usecase:PrescricaoListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
