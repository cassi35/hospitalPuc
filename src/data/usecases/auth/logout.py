from src.domain.usecases.auth.logout import LogoutUseCase
from typing import Dict
from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from src.errors.types.InvalidToken import InvalidToken
from src.errors.types.AcessTokenRequired import AcessTokenRequired
from src.errors.types.http_bad_request import HttpBadRequestError

class LogoutUseCaseImpl(LogoutUseCase):
    def __init__(self, auth_cache: AuthCacheInterface, jwt_service: JWTServiceInterface):
        self.auth_cache = auth_cache
        self.jwt_service = jwt_service
        self.token_data = None
    
    def logout(self, token: str) -> Dict:
        self.__validate_token(token=token)
        self.__decode_token(token=token)
        self.__blacklist_token()
        return self.__format_response()
    
    def __validate_token(self, token: str) -> None:
        """Valida se o token foi fornecido"""
        if not token or len(token.strip()) == 0:
            raise HttpBadRequestError("Token é obrigatório")
    
    def __decode_token(self, token: str) -> None:
        """Decodifica e valida o token"""
        # Verifica se o token é válido (estrutura + expiração)
        if not self.jwt_service.is_token_valid(token):
            raise InvalidToken("Token inválido ou expirado")
        
        # Decodifica o token
        self.token_data = self.jwt_service.decode_token(token)
        
        # Verifica se é um access token (não refresh token)
        if self.token_data.get("refresh", False):
            raise AcessTokenRequired("Logout deve ser feito com access token, não refresh token")
    
    def __blacklist_token(self) -> None:
        """Adiciona o token na blacklist (cache)"""
        jti = self.token_data.get("jti")
        if not jti:
            raise InvalidToken("Token não possui JTI válido")
        
        # Calcula o tempo de expiração do token para definir TTL do cache
        exp = self.token_data.get("exp")
        if exp:
            # TTL = tempo restante até expiração do token
            from datetime import datetime, timezone
            ttl = exp - int(datetime.now(timezone.utc).timestamp())
            if ttl > 0:
                # Armazena na blacklist com TTL
                self.auth_cache.set_temp_token(key=f"blacklist:{jti}", value={"revoked": True}, ttl=ttl)
    
    def __format_response(self) -> Dict:
        """Formata a resposta de sucesso"""
        return {
            "success": True,
            "message": "Logout realizado com sucesso"
        }