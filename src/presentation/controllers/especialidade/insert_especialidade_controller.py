from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.especialidade.insert_especialidade import EspecialidadeInsertUseCase as EspecialidadeInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
class EspecialidadeInsertController(ControllerInterface):
    def __init__(self,usecase:EspecialidadeInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        especialidade = EspecialidadeDomain(**http_request.body)
        response = self.usecase.insert(
            especialidade=especialidade
        )
        return HTTPResponse(status_code=200,body=response)
