from src.presentation.controllers.medico.list_medico_controller import MedicoListController
from tests.data.mock.medico.list_medico_spy import MedicoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = MedicoListUsecaseSpy()
    controller = MedicoListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
