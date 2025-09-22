from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.medicamento.insert_medicamento import MedicamentoInsertUseCase as MedicamentoInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain
class MedicamentoInsertController(ControllerInterface):
    def __init__(self,usecase:MedicamentoInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        medicamento = MedicamentoDomain(**http_request.body)
        response = self.usecase.insert(
            medicamento=medicamento
        )
        return HTTPResponse(status_code=200,body=response)
