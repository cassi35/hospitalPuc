from src.presentation.controllers.endereco.list_endereco_controller import EnderecoListController
from tests.data.mock.endereco.list_endereco_spy import EnderecoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EnderecoListUsecaseSpy()
    endereco_list_controller = EnderecoListController(
        usecase=usecase_spy
    )
    response = endereco_list_controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)