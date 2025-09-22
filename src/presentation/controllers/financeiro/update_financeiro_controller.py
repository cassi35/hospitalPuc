from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.financeiro.update_financeiro import FinanceiroUpdateUseCase as FinanceiroUpdateInterface
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
class FinanceiroUpdateController(ControllerInterface):
    def __init__(self,usecase:FinanceiroUpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        financeiro_id = int(http_request.path_params["id"])
        financeiro = FinanceiroDomain(**http_request.body) 
        financeiro.id = financeiro_id
        response = self.usecase.update(
            financeiro_id=financeiro_id,
            financeiro=financeiro
        )
        return HTTPResponse(status_code=200,body=response)
