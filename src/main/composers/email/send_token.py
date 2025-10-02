from src.presentation.controllers.email.send_token import SendVerificationTokenController
from src.data.usecases.email.send_token import SendVerificationTokenUsecase
from src.infra.email.stmp_adapter_service import SMTPEmailService
def send_verification_token_composer():
    stmp = SMTPEmailService()
    usecase = SendVerificationTokenUsecase(email_service=stmp)
    controller = SendVerificationTokenController(usecase=usecase)
    return controller.handle