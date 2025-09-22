from src.presentation.controllers.leito.list_leito_controller import LeitoListController
from tests.data.mock.leito.list_leito_spy import LeitoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = LeitoListUsecaseSpy()
    controller = LeitoListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
