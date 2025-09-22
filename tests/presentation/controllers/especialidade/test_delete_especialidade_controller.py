from src.presentation.controllers.especialidade.delete_especialidade_controller import EspecialidadeDeleteController
from tests.data.mock.especialidade.delete_especialidade_spy import EspecialidadeDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EspecialidadeDeleteUsecaseSpy()
    controller = EspecialidadeDeleteController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
