from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medico.insert_medico import MedicoInsertUseCase as MedicoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.medico_model import Medico as MedicoDomain
class MedicoInsertController(ControllerInterface):
    def __init__(self,usecase:MedicoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        medico = MedicoDomain(**http_request.body)
        response = self.usecase.insert(
            medico=medico
        )
        return HTTPResponse(status_code=200,body=response)
