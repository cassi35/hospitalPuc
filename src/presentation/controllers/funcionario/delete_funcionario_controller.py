from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.funcionario.delete_funcionario import FuncionarioDeleteUseCase as FuncionarioDeleteInterface
class FuncionarioDeleteController(ControllerInterface): 
    def __init__(self,usecase:FuncionarioDeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        funcionario_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            funcionario_id=funcionario_id
        )
        return HTTPResponse(status_code=200,body=response)
