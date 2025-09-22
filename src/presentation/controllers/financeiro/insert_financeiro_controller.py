from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase as FinanceiroInsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
class FinanceiroInsertController(ControllerInterface):
    def __init__(self,usecase:FinanceiroInsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        financeiro = FinanceiroDomain(**http_request.body)
        response = self.usecase.insert(
            financeiro=financeiro
        )
        return HTTPResponse(status_code=200,body=response)
