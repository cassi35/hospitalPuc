from src.presentation.controllers.setor.list_setor_controller import SetorListController
from tests.data.mock.setor.list_setor_spy import SetorListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = SetorListUsecaseSpy()
    controller = SetorListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
