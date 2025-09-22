from src.presentation.controllers.consulta.list_consulta_controller import ConsultaListController
from tests.data.mock.consulta.list_consulta_spy import ConsultaListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConsultaListUsecaseSpy()
    controller = ConsultaListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
