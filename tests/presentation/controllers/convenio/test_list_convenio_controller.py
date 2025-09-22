from src.presentation.controllers.convenio.list_convenio_controller import ConvenioListController
from tests.data.mock.convenio.list_convenio_spy import ConvenioListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConvenioListUsecaseSpy()
    convenio_list_controller = ConvenioListController(
        usecase=usecase_spy
    )
    response = convenio_list_controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response)