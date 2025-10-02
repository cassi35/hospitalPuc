from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.email.send_token import SendVerificationTokenUsecase
from src.domain.models.user_email import UserEmail as UserEmailDomain
class SendVerificationTokenController(ControllerInterface):
    def __init__(self,usecase:SendVerificationTokenUsecase):
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        email = UserEmailDomain(**http_request.body)
        response = self.usecase.send_email(token=email.token,email=email.email)
        return HTTPResponse(status_code=200,body=response)