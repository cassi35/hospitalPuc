from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.funcionario.insert_funcionario import FuncionarioInsertUseCase as FuncionarioInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
class FuncionarioInsertController(ControllerInterface):
    def __init__(self,usecase:FuncionarioInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        funcionario = FuncionarioDomain(**http_request.body)
        response = self.usecase.insert(
            funcionario=funcionario
        )
        return HTTPResponse(status_code=200,body=response)
