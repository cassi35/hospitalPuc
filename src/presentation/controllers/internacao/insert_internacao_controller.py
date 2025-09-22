from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.internacao.insert_internacao import InternacaoInsertUseCase as InternacaoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.internacao_model import Internacao as InternacaoDomain
class InternacaoInsertController(ControllerInterface):
    def __init__(self,usecase:InternacaoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        internacao = InternacaoDomain(**http_request.body)
        response = self.usecase.insert(
            internacao=internacao
        )
        return HTTPResponse(status_code=200,body=response)
