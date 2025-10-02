from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.email.send_welcome import SendWelcomeEmailUsecase
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.user_email import UserEmail as UserEmailDomain
class SendWelcomeEmailController(ControllerInterface):
    def __init__(self,usecase:SendWelcomeEmailUsecase):
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        email = UserEmailDomain(**http_request.body)
        response = self.usecase.send_email(email=email.email,name=email.name)
        return HTTPResponse(status_code=200,body=response)
    