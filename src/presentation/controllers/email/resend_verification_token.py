from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.email.resend_verification_token import ResendVerificationTokenUsecase
from src.domain.models.user_email import UserEmail as UserEmailDomain
class ResendVerificationTokenController(ControllerInterface):
    def __init__(self,usecase:ResendVerificationTokenUsecase):
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        email = UserEmailDomain(**http_request.body)
        response = self.usecase.send_email(email=email.email,token=email.token)
        return HTTPResponse(status_code=200,body=response)