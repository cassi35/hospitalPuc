from src.data.usecases.auth.forgot_password import ForgotPasswordUsecase
from src.data.usecases.auth.login import LoginUseCaseImpl
from src.data.usecases.auth.logout import LogoutUseCaseImpl
from src.data.usecases.auth.reset_password import ResetPasswordUseCase
from src.data.usecases.auth.signup import SignupUseCaseImpl
from src.data.usecases.auth.verify_email import VerifyEmailUseCaseImpl
from src.infra.db.repositories.auth_repository import AuthRepository
from src.infra.email.stmp_adapter_service import SMTPEmailService
from src.infra.services.jwt_service import JWTService
from src.infra.services.auth_cahe_service import AuthCacheService
from src.infra.services.password_service import PasswordService
from src.infra.services.url_safe_token import URLSafeTokenService
from src.domain.models.auth_model import AuthModel
import pytest
jwt_service = JWTService()
auth_cache_service = AuthCacheService()
password_service = PasswordService()
url_safe_token_service = URLSafeTokenService()
email_service = SMTPEmailService()
auth_repository = AuthRepository()
@pytest.mark.skip(reason="teste realizado com sucesso")

def test_signup_usecase():
    signup_usecase = SignupUseCaseImpl(
          auth_cache=auth_cache_service,
          auth_repository=auth_repository,
          email_service=email_service,
          jwt_service=jwt_service,
          password_service=password_service,
          token_service=url_safe_token_service
     )
    email = "sobralcassique@gmail.com"
    senha = "12345687"
    role = "Paciente"
    nome = 'cassiano'
    auth = {
        "email": email,
        "senha": senha,
        "role": role,
        "nome": nome
    }
    response = signup_usecase.signup(
        auth=auth
    )
#     print(response)
# @pytest.mark.skip(reason="teste realizado com sucesso")
def test_verify_email_usecase():
    verify_email_usecase = VerifyEmailUseCaseImpl(
        auth_cache=auth_cache_service,
        auth_repository=auth_repository,
        jwt_service=jwt_service,
        token_service=url_safe_token_service,
        email_service=email_service
    )
    email = "sobralcassique@gmail.com"
    token =  ".eJyrVkrNTczMUbJSKs5PKkrMSU4sLs4sLE11SAcJ6yXn5yrpKBWn5mUkApUYGhmbmJpZmAOFivJzUoEiAYnJmal5JalAkbz8XJAI2IDEvHylWgBzex2z.aO-o9Q.ODJk5Vb63lqDcuKgq82Hk1wo8UM"
    response = verify_email_usecase.verify(
        email=email,
        token=token,
    )
    print(response)
