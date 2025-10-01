from src.domain.models.user_email import UserEmail
from src.infra.email.stmp_adapter_service import SMTPEmailService   
import pytest
stmp_service = SMTPEmailService()
@pytest.mark.skip(reason="sucesso")
def test_send_welcome_email():
    user_email = UserEmail(
        email="sobralcassique@gmail.com",
        name="Cassique Sobral"
    )
    response = stmp_service.send_welcome_email(user=user_email)
    print(response)
@pytest.mark.skip(reason="sucesso")

def test_send_token():
    email = "sobralcassique@gmail.com"
    token = 4421
    response = stmp_service.send_token(email=email,token=token)
    print(response)
@pytest.mark.skip(reason="sucesso")
def test_send_reset_password_email():
    email = "sobralcassique@gmail.com"
    token = 4421
    response = stmp_service.send_reset_password_email(email=email, token=token)
    print(response)
def test_resend_verification_token():
    email = "sobralcassique@gmail.com"
    token = 4421
    response = stmp_service.resend_verification_token(email=email, token=token)
    print(response)