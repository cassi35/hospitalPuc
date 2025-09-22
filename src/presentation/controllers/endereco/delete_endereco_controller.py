from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.endereco.delete_endereco import EnderecoDeleteUseCase as EnderecoDeleteInterface
class EnderecoDeleteController(ControllerInterface): 
    def __init__(self,usecase:EnderecoDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        endereco_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            endereco_id=endereco_id
        )
        return HTTPResponse(status_code=200,body=response)