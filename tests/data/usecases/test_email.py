from src.data.usecases.email.send_welcome import SendWelcomeEmailUsecase
from src.data.usecases.email.resend_verification_token import ResendVerificationTokenUsecase
from src.data.usecases.email.send_token import SendVerificationTokenUsecase
from src.data.usecases.email.send_reset_password import ResetPasswordEmailUsecase
from tests.infra.emails.stmp_emailService_spy import StmpEmailServiceSpy
from src.domain.models.user_email import UserEmail as UserEmailDomain
from tests.infra.repositories.funcionario_repository_spy import FuncionarioRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.funcionario_repository_spy import FuncionarioRepositorySpy
import pytest
@pytest.mark.skip(reason="teste com sucesso")
def test_send_welcome_email():
    stpm_service_spy = StmpEmailServiceSpy()
    funcionario = FuncionarioRepositorySpy()
    medico = MedicoRepositorySpy()
    paciente = PacienteRepositorySpy()
    usecase = SendWelcomeEmailUsecase(
        email_service=stpm_service_spy,
        funcionario_repository=funcionario,
        medico_repository=medico,
        paciente_repository=paciente
    )
    user_email = UserEmailDomain(
email='sobral@gmail.com',
name='Sobral',
token=1231
    )
    response = usecase.send_email(email=user_email.email,name=user_email.name)
    print()
    print(response)
@pytest.mark.skip(reason="teste com sucesso")
def test_send_token_email():
    stmp_service_spy = StmpEmailServiceSpy()
    usecase = SendVerificationTokenUsecase(email_service=stmp_service_spy)
    user_email = UserEmailDomain(
email='sobral@gmail.com',
name='Sobral',
token=1231
    )
    response = usecase.send_email(email=user_email.email,token=user_email.token)
    print(response)
@pytest.mark.skip(reason="teste com sucesso")

def test_resend_verification_token():
    stmp_service_spy = StmpEmailServiceSpy()
    usecase = ResendVerificationTokenUsecase(
        email_service=stmp_service_spy
    )
    user_email = UserEmailDomain(
email='sobral@gmail.com',
name='Sobral',
token=1231
    )
    response = usecase.send_email(email=user_email.email,token=user_email.token)
    print(response)
def test_send_reset_password():
    stmp_service_spy = StmpEmailServiceSpy()
    usecase = ResetPasswordEmailUsecase(
        email_service=stmp_service_spy,
        funcionario_repository=FuncionarioRepositorySpy(),
        medico_repository=MedicoRepositorySpy(),
        paciente_repository=PacienteRepositorySpy()
    )
    user_email = UserEmailDomain(
email='sobral@gmail.com',
name='Sobral',
token=1231
    )
    response = usecase.send_email(
        email=user_email.email,
        token=user_email.token

    )
    print(response)