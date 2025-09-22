from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.convenio.update_convenio import ConvenioUpdateUseCase as ConvenioUpdateInterface
from src.domain.models.convenio_model import Convenio as ConvenioDomain
class ConvenioUpdateController(ControllerInterface):
    def __init__(self,usecase:ConvenioUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        convenio_id = int(http_request.path_params["id"])
        convenio = ConvenioDomain(**http_request.body) 
        convenio.id = convenio_id
        response = self.usecase.update(
            convenio_id=convenio_id,
            convenio=convenio
        )
        return HTTPResponse(status_code=200,body=response)
