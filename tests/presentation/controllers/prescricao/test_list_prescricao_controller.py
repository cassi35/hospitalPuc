from src.presentation.controllers.prescricao.list_prescricao_controller import PrescricaoListController
from tests.data.mock.prescricao.list_prescricao_spy import PrescricaoListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = PrescricaoListUsecaseSpy()
    controller = PrescricaoListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
