from src.presentation.controllers.internacao.list_internacao_controller import InternacaoListController
from tests.data.mock.internacao.list_internacao_spy import InternacaoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = InternacaoListUsecaseSpy()
    controller = InternacaoListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
