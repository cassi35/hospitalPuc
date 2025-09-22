from src.presentation.controllers.prescricao.delete_prescricao_controller import PrescricaoDeleteController
from tests.data.mock.prescricao.delete_prescricao_spy import PrescricaoDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = PrescricaoDeleteUsecaseSpy()
    controller = PrescricaoDeleteController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
