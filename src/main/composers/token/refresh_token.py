from src.data.usecases.token.refresh_token import RefreshTokenImpl
from src.infra.services.jwt_service import JWTService
def refresh_token_usecase_composer():
    jwt_service = JWTService()
    return RefreshTokenImpl(
        jwt_service=jwt_service
    )