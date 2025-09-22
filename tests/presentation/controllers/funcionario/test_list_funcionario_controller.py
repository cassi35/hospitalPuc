from src.presentation.controllers.funcionario.list_funcionario_controller import FuncionarioListController
from tests.data.mock.funcionario.list_funcionario_spy import FuncionarioListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = FuncionarioListUsecaseSpy()
    controller = FuncionarioListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
