from tests.data.mock.convenio.update_convenio_spy import ConvenioUpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.convenio.update_convenio_controller import ConvenioUpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = {
            "nome": "Unimed",
            "tipo_plano":"Familiar"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConvenioUpdateUsecaseSpy()
    convenio_update_controller = ConvenioUpdateController(usecase_spy)
    response = convenio_update_controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response)