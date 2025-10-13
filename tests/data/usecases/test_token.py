from src.data.usecases.token.access_token import AccessTokenUsecaseImpl
from src.data.usecases.token.refresh_token import RefreshTokenImpl
from src.data.usecases.token.role_checker import RoleCheckerUsecaseImpl
from tests.infra.mock.services.auth_service_spy import AuthServiceSpy
from tests.infra.mock.services.jwt_service_spy import JWTServiceSpy
import pytest
jwt_service = JWTServiceSpy()
auth_service = AuthServiceSpy()
@pytest.mark.skip(reason="success")
def test_access_token_usecase():
    usecase = AccessTokenUsecaseImpl(auth_cache=auth_service,jwt_service=jwt_service)
    token = usecase.verify_access(token="valid_token"
                                  ) 
    print(token)
@pytest.mark.skip(reason="success")
def test_refresh_token_usecase():
    usecase = RefreshTokenImpl(jwt_service=jwt_service)
    token = usecase.verify_refresh(token="valid_token")
    print(token)
def test_role_checker_usecase():
    usecase = RoleCheckerUsecaseImpl()
    role = usecase.check_role(
        allowed_roles=["Paciente","Medico"],
        user_data={"id":1,"name":"John Doe","is_verified": True,"role":"Medico"}
    )
    assert role == True