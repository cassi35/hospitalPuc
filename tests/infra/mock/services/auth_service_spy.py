from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
class AuthServiceSpy(AuthCacheInterface):
    def __init__(self):
        self.blacklist_tokens = set()
        self.is_token_blacklisted_call_count = 0
        self.blacklist_token_call_count = 0
        self.is_token_blacklisted_attributes = {}
        self.blacklist_token_attributes = {}
    def blacklist_token(self, token: str, ttl: int) -> bool:
        self.blacklist_token_attributes = {
            "token": token,
            "ttl": ttl
        }
        