from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.internacao.delete_internacao import InternacaoDeleteUseCase as InternacaoDeleteInterface
class InternacaoDeleteController(ControllerInterface): 
    def __init__(self,usecase:InternacaoDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        internacao_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            internacao_id=internacao_id
        )
        return HTTPResponse(status_code=200,body=response)
