from src.presentation.controllers.leito.delete_leito_controller import LeitoDeleteController
from tests.data.mock.leito.delete_leito_spy import LeitoDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = LeitoDeleteUsecaseSpy()
    controller = LeitoDeleteController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
