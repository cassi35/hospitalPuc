from src.presentation.controllers.endereco.delete_endereco_controller import EnderecoDeleteController
from tests.data.mock.endereco.delete_endereco_spy import EnderecoDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EnderecoDeleteUsecaseSpy()
    endereco_delete_controller = EnderecoDeleteController(
        usecase_spy
    )
    response = endereco_delete_controller.handle(http_request_mock)
    print()
    print(response.status_code)