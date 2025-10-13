from src.domain.usecases.token.refresh_token import RefreshTokenUsecase
from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from src.errors.types.RefreshTokenRequired import RefreshTokenRequired
from src.errors.types.InvalidToken import InvalidToken

class RefreshTokenImpl(RefreshTokenUsecase):
    def __init__(self, jwt_service: JWTServiceInterface):
        self.jwt_service = jwt_service
    
    def verify_refresh(self, token: str) -> dict:
        if not token:
            raise RefreshTokenRequired("Refresh token is required")
        if not self.jwt_service.is_token_valid(token):
            raise InvalidToken("Invalid or expired token")
        decoded = self.jwt_service.decode_token(token)
        if not decoded.get("refresh", False):
            raise RefreshTokenRequired("Refresh token required, but access token provided")
        return decoded