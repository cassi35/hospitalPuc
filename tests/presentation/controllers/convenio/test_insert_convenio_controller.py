from src.presentation.controllers.convenio.insert_convenio_controller import ConvenioInsertController
from  tests.data.mock.convenio.insert_convenio_spy import ConvenioInsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self)-> None:
        self.body = {
            "nome": "Unimed",
            "tipo_plano":"Individual"
        }
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ConvenioInsertUsecaseSpy()
    convenio_insert_controller = ConvenioInsertController(usecase_spy)
    response = convenio_insert_controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
        