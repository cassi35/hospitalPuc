from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.exame.update_exame import ExameUpdateUseCase as ExameUpdateInterface
from src.domain.models.exame_model import Exame as ExameDomain
class ExameUpdateController(ControllerInterface):
    def __init__(self,usecase:ExameUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        exame_id = int(http_request.path_params["id"])
        exame = ExameDomain(**http_request.body) 
        exame.id = exame_id
        response = self.usecase.update(
            exame_id=exame_id,
            exame=exame
        )
        return HTTPResponse(status_code=200,body=response)
