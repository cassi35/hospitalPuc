from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.setor.list_setor import SetorListUseCase as SetorListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class SetorListController(ControllerInterface):
    def __init__(self,usecase:SetorListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
