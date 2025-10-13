from src.domain.usecases.token.access_token import AccessTokenUsecase
from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.errors.types.InvalidToken import InvalidToken
from src.errors.types.AcessTokenRequired import AcessTokenRequired

class AccessTokenUsecaseImpl(AccessTokenUsecase):
    def __init__(self, jwt_service: JWTServiceInterface, auth_cache: AuthCacheInterface):
        self.jwt_service = jwt_service
        self.auth_cache = auth_cache
    
    def verify_access(self, token: str) -> dict:
        if not token:
            raise AcessTokenRequired("Access token is required")
        if not self.jwt_service.is_token_valid(token):
            raise InvalidToken("Invalid or expired token")
        decoded = self.jwt_service.decode_token(token)
        if decoded.get("refresh", False):
            raise AcessTokenRequired("Access token required, but refresh token provided")
        jti = decoded.get("jti")
        if jti and self.auth_cache.is_token_blacklisted(jti):
            raise InvalidToken("Token was revoked")
        return decoded