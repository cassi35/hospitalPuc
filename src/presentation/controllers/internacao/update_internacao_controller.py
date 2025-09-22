from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.internacao.update_internacao import InternacaoUpdateUseCase as InternacaoUpdateInterface
from src.domain.models.internacao_model import Internacao as InternacaoDomain
class InternacaoUpdateController(ControllerInterface):
    def __init__(self,usecase:InternacaoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        internacao_id = int(http_request.path_params["id"])
        internacao = InternacaoDomain(**http_request.body) 
        internacao.id = internacao_id
        response = self.usecase.update(
            internacao_id=internacao_id,
            internacao=internacao
        )
        return HTTPResponse(status_code=200,body=response)
