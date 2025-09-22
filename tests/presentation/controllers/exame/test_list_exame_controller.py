from src.presentation.controllers.exame.list_exame_controller import ExameListController
from tests.data.mock.exame.list_exame_spy import ExameListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ExameListUsecaseSpy()
    controller = ExameListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
