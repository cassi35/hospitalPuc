from src.data.usecases.token.access_token import AccessTokenUsecaseImpl
from src.infra.services.jwt_service import JWTService
from src.infra.services.auth_cahe_service import AuthCacheService
def access_token_usecase_composer():
    jwt_service = JWTService()
    auth_cache = AuthCacheService()
    return AccessTokenUsecaseImpl(
        jwt_service=jwt_service, 
        auth_cache=auth_cache
    )