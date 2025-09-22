from src.presentation.controllers.convenio.delete_convenio_controller import ConvenioDeleteController
from tests.data.mock.convenio.delete_convenio_spy import ConvenioDeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConvenioDeleteUsecaseSpy()
    convenio_delete_controller = ConvenioDeleteController(usecase_spy)
    response = convenio_delete_controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None