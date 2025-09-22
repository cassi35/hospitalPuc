from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.convenio.insert_convenio import ConvenioInsertUseCase as ConvenioInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.convenio_model import Convenio as ConvenioDomain
class ConvenioInsertController(ControllerInterface):
    def __init__(self,usecase:ConvenioInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        convenio = ConvenioDomain(**http_request.body)
        response = self.usecase.insert(
            convenio=convenio
        )
        return HTTPResponse(status_code=200,body=response)
