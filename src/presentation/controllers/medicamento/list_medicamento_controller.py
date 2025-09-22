from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.medicamento.list_medicamento import MedicamentoListUseCase as MedicamentoListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class MedicamentoListController(ControllerInterface):
    def __init__(self,usecase:MedicamentoListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
