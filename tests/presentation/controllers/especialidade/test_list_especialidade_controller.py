from src.presentation.controllers.especialidade.list_especialidade_controller import EspecialidadeListController
from tests.data.mock.especialidade.list_especialidade_spy import EspecialidadeListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = EspecialidadeListUsecaseSpy()
    controller = EspecialidadeListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
