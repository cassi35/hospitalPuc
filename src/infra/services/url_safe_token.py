from itsdangerous import URLSafeTimedSerializer
import logging
from src.config import Settings
from src.data.interfaces.urSafeTokenService_interface import URSafeTokenServiceInterface
class URLSafeTokenService(URSafeTokenServiceInterface):
    def __init__(self):
        self.secret_Key = Settings().JWT_SECRET
        self.salt = "email-confirmation"
        self.serializer = URLSafeTimedSerializer(self.secret_Key)
    def create_url_safe_token(self, data:dict) ->str:
        token = self.serializer.dumps(data, salt=self.salt)
        return token
    def decode_url_safe_token(self, token:str)-> dict:
        try:
            data = self.serializer.loads(token, salt=self.salt)  # ✅ usa o mesmo salt!
            return data
        except Exception as e:
            logging.error(f"Erro ao verificar o token: {e}")
            raise e