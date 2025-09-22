from src.presentation.controllers.financeiro.list_financeiro_controller import FinanceiroListController
from tests.data.mock.financeiro.list_financeiro_spy import FinanceiroListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = FinanceiroListUsecaseSpy()
    controller = FinanceiroListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
