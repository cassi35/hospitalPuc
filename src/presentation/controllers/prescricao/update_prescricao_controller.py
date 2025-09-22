from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.prescricao.update_prescricao import PrescricaoUpdateUseCase as PrescricaoUpdateInterface
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
class PrescricaoUpdateController(ControllerInterface):
    def __init__(self,usecase:PrescricaoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        prescricao_id = int(http_request.path_params["id"])
        prescricao = PrescricaoDomain(**http_request.body) 
        prescricao.id = prescricao_id
        response = self.usecase.update(
            prescricao_id=prescricao_id,
            prescricao=prescricao
        )
        return HTTPResponse(status_code=200,body=response)
