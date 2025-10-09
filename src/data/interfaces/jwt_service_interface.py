from abc import ABC,abstractmethod
from typing import Optional
from datetime import timedelta
class JWTServiceInterface(ABC):
    @abstractmethod
    def create_access_token(self,user_data:dict,expiry:timedelta = None ,refresh_token:bool = False)->str:pass
    @abstractmethod
    def decode_token(self,token:str)-> Optional[dict]:pass 