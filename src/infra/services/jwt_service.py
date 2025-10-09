from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from datetime import timedelta,datetime
from typing import Optional
import jwt
import uuid
import logging
from src.config import Config
class JWTService(JWTServiceInterface):
    def __init__(self):
        self.secret = Config.JWT_SECRET
        self.algorithm = Config.JWT_ALGORITHM
    def create_access_token(self, user_data: dict, expiry: Optional[timedelta] = None,refresh_token:bool = False) -> str:
        payload = {}
        payload['user_data'] = user_data
        payload['exp'] = datetime.now()+expiry if expiry is not None else timedelta( minutes=15)
        payload['jti'] = str(uuid.uuid4())
        payload['refresh'] = refresh_token
        token = jwt.encode(
            payload=payload,
            key=self.secret,
            algorithm=self.algorithm
        )
        return token
    def decode_token(self, token:str)-> Optional[dict]:
        try:
            token_data = jwt.decode(
                jwt=token,
                key=self.secret,
                algorithms=[self.algorithm]
            )
            return token_data
        except jwt.ExpiredSignatureError:
            logging.error("Token expirado")
            raise Exception("Token expirado")
        except jwt.InvalidTokenError:
            logging.error("Token inválido")
            raise Exception("Token inválido")
        except jwt.PyJWTError as e:
            logging.error(f"Erro ao decodificar token: {e}")
            raise Exception("Erro ao decodificar token: " + str(e))