from src.data.interfaces.auth_cahce_interface import AuthCacheInterface
from src.config import Config
from src.infra.cache.connection import CacheConnectionHandler
import logging
from typing import Optional

class AuthCacheService(AuthCacheInterface):
    def __init__(self):
        self.redis = CacheConnectionHandler().create_redis_connection()
        self.blacklist_prefix = Config.REDIS_BLACKLIST_PREFIX

    def blacklist_token(self, token: str, ttl: int) -> bool:
        """
        Adiciona o token (jti) à blacklist do Redis com tempo de expiração (ttl).
        """
        try:
            key = f"{self.blacklist_prefix}{token}"
            self.redis.set(key, "1", ex=ttl)
            return True
        except Exception as e:
            logging.error(f"Erro ao adicionar token à blacklist: {e}")
            return False

    def is_token_blacklisted(self, token: str) -> bool:
        """
        Verifica se o token (jti) está na blacklist do Redis.
        """
        try:
            key = f"{self.blacklist_prefix}{token}"
            return self.redis.exists(key) != '0'
        except Exception as e:
            logging.error(f"Erro ao verificar token na blacklist: {e}")
            return False

    def store_temp_token(self, key: str, token: str, ttl: int = 900) -> bool:
        """
        Armazena um token temporário (ex: para reset de senha) no Redis.
        """
        try:
            self.redis.set(key, token, ex=ttl)
            return True
        except Exception as e:
            logging.error(f"Erro ao armazenar token temporário: {e}")
            return False

    def get_temp_token(self, key: str) -> Optional[str]:
        """
        Recupera um token temporário do Redis.
        """
        value = self.redis.get(key)
        if value is not None:
            return value 
        return None

    def delete_temp_token(self, key: str) -> bool:
        """
        Remove um token temporário do Redis.
        """
        try:
            token = self.get_temp_token(key)
            if token == None:
                logging.warning(f"Token com chave {key} não encontrado para deleção.")
                return False
            delete = self.redis.delete(key)
            if delete == 1:
                return True
            return False
        except Exception as e:
            logging.error(f"Erro ao deletar token temporário: {e}")
            return False