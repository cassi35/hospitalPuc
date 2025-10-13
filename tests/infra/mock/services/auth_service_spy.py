from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from typing import Optional,Dict,Any
class AuthServiceSpy(AuthCacheInterface):
    def __init__(self):
        pass 
    def blacklist_token(self, token: str, ttl: int) -> bool:
        return True
    def is_token_blacklisted(self, token: str) -> bool:
        return False
    def store_temp_token(self, key: str, value: Dict[str, Any], ttl: int = 900) -> bool:
        return True
    def get_temp_token(self, key: str) -> Optional[Dict[str, Any]]:
        return {"user_id": "any_id"}
    def delete_temp_token(self, key: str) -> bool:
        return True