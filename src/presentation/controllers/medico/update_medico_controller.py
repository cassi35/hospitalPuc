from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medico.update_medico import MedicoUpdateUseCase as MedicoUpdateInterface
from src.domain.models.medico_model import Medico as MedicoDomain
class MedicoUpdateController(ControllerInterface):
    def __init__(self,usecase:MedicoUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        medico_id = int(http_request.path_params["id"])
        medico = MedicoDomain(**http_request.body) 
        medico.id = medico_id
        response = self.usecase.update(
            medico_id=medico_id,
            medico=medico
        )
        return HTTPResponse(status_code=200,body=response)
