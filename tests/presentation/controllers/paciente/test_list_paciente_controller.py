from src.presentation.controllers.paciente.list_paciente_controller import PacienteListController
from tests.data.mock.paciente.list_paciente_spy import PacienteListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = PacienteListUsecaseSpy()
    controller = PacienteListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
