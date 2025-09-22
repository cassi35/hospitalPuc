from src.presentation.controllers.setor.delete_setor_controller import SetorDeleteController
from tests.data.mock.setor.delete_setor_spy import SetorDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = SetorDeleteUsecaseSpy()
    controller = SetorDeleteController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
