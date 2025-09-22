from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.funcionario.update_funcionario import FuncionarioUpdateUseCase as FuncionarioUpdateInterface
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
class FuncionarioUpdateController(ControllerInterface):
    def __init__(self,usecase:FuncionarioUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        funcionario_id = int(http_request.path_params["id"])
        funcionario = FuncionarioDomain(**http_request.body) 
        funcionario.id = funcionario_id
        response = self.usecase.update(
            funcionario_id=funcionario_id,
            funcionario=funcionario
        )
        return HTTPResponse(status_code=200,body=response)
