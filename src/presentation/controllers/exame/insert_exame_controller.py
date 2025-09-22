from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.exame.insert_exame import ExameInsertUseCase as ExameInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.exame_model import Exame as ExameDomain
class ExameInsertController(ControllerInterface):
    def __init__(self,usecase:ExameInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        exame = ExameDomain(**http_request.body)
        response = self.usecase.insert(
            exame=exame
        )
        return HTTPResponse(status_code=200,body=response)
