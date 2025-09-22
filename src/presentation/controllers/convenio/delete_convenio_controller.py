from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.convenio.delete_convenio import ConvenioDeleteUseCase as ConvenioDeleteInterface
class ConvenioDeleteController(ControllerInterface): 
    def __init__(self,usecase:ConvenioDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        convenio_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            convenio_id=convenio_id
        )
        return HTTPResponse(status_code=200,body=response)
