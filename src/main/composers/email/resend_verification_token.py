from src.presentation.controllers.email.resend_verification_token import ResendVerificationTokenController
from src.data.usecases.email.resend_verification_token import ResendVerificationTokenUsecase
from src.infra.email.stmp_adapter_service import SMTPEmailService
def resend_verification_token_composer():
    stmp = SMTPEmailService()
    usecase = ResendVerificationTokenUsecase(
        email_service=stmp
    )
    controller = ResendVerificationTokenController(usecase=usecase)
    return controller.handle