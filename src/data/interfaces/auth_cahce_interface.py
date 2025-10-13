

# Interface mais clara para JWT + Cache
from abc import ABC, abstractmethod
from typing import Optional,Dict,Any

class AuthCacheInterface(ABC):
    # Para controle de tokens (não sessão tradicional)
    @abstractmethod
    def blacklist_token(self, token: str, ttl: int) -> bool:
        """Invalida JWT token (logout/revogação)"""
        pass
    
    @abstractmethod
    def is_token_blacklisted(self, token: str) -> bool:
        """Verifica se JWT foi invalidado"""
        pass
    
    # Para tokens temporários (reset senha, verificação email)
    @abstractmethod
    def store_temp_token(self, key: str, value: Dict[str, Any], ttl: int = 900) -> bool:
        """Armazena token temporário (15 min)"""
        pass
    
    @abstractmethod
    def get_temp_token(self, key: str) -> Optional[Dict[str, Any]]:
        """Recupera token temporário"""
        pass
    
    @abstractmethod
    def delete_temp_token(self, key: str) -> bool:
        """Remove token após uso"""
        pass






# essa interface define métodos para armazenar e recuperar sessões de usuário e tokens de autenticação em um cache (ex: Redis).
# from abc import ABC, abstractmethod
# from typing import Optional, Dict

# class AuthCacheInterface(ABC):
#     @abstractmethod
#     def store_session(self, user_id: int, session_data: dict, ttl: int = 3600) -> bool:
#         """Armazena sessão do usuário"""
#         pass
    
#     @abstractmethod
#     def get_session(self, user_id: int) -> Optional[dict]:
#         """Recupera sessão do usuário"""
#         pass
    
#     @abstractmethod
#     def invalidate_session(self, user_id: int) -> bool:
#         """Invalida sessão do usuário"""
#         pass
    
#     @abstractmethod
#     def store_reset_token(self, email: str, token: str, ttl: int = 1800) -> bool:
#         """Armazena token de reset (30 min)"""
#         pass
    
#     @abstractmethod
#     def get_reset_token(self, email: str) -> Optional[str]:
#         """Recupera token de reset"""
#         pass
    
#     @abstractmethod
#     def blacklist_token(self, token: str, ttl: int) -> bool:
#         """Adiciona token à blacklist"""
#         pass
    
#     @abstractmethod
#     def is_token_blacklisted(self, token: str) -> bool:
#         """Verifica se token está na blacklist"""
#         pass