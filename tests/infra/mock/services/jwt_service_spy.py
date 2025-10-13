from src.data.interfaces.jwt_service_interface import JWTServiceInterface
from typing import Optional

class JWTServiceSpy(JWTServiceInterface):
    def __init__(self):
        self.encrypt_called_with = None
        self.decrypt_called_with = None
        self.encrypt_return_value = 'any_token'
        self.decrypt_return_value = {'user_id': 'any_id'}
        
        # ✅ NOVO: Controlar diferentes cenários de teste
        self.should_return_valid = True
        self.token_type = "refresh"  # "access" ou "refresh"

    def create_access_token(self, user_data, expiry=None, refresh_token=False) -> str:
        self.encrypt_called_with = {
            'user_data': user_data,
            'expiry': expiry,
            'refresh_token': refresh_token
        }
        return self.encrypt_return_value 
    
    def decode_token(self, token: str) -> Optional[dict]:
        self.decrypt_called_with = token
        
        # ✅ NOVO: Retorna dados diferentes baseado no tipo de token configurado
        if self.token_type == "refresh":
            return {
                'user_id': 'any_id',
                'refresh': True,  # ✅ CRUCIAL: Marca como refresh token
                'jti': 'any_jti'
            }
        else:  # access token
            return {
                'user_id': 'any_id',
                'refresh': False,  # ✅ CRUCIAL: Marca como access token
                'jti': 'any_jti'
            }
    
    def is_token_valid(self, token: str) -> bool:
        self.decrypt_called_with = token
        return self.should_return_valid