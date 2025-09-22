from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.prescricao.insert_prescricao import PrescricaoInsertUseCase as PrescricaoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
class PrescricaoInsertController(ControllerInterface):
    def __init__(self,usecase:PrescricaoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        prescricao = PrescricaoDomain(**http_request.body)
        response = self.usecase.insert(
            prescricao=prescricao
        )
        return HTTPResponse(status_code=200,body=response)
