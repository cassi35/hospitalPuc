from src.presentation.controllers.medicamento.list_medicamento_controller import MedicamentoListController
from tests.data.mock.medicamento.list_medicamento_spy import MedicamentoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = MedicamentoListUsecaseSpy()
    controller = MedicamentoListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
