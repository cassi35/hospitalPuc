from abc import ABC,abstractmethod
from src.domain.models.auth_model import AuthModel
from typing import Dict,Optional
class AuthRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self,user_data:dict)-> None:
        pass
    @abstractmethod
    def get_user_by_email(self,email:str)->AuthModel:
        pass
    @abstractmethod
    def get_user_by_id(self,user_id:int)-> AuthModel:
        pass
    @abstractmethod
    def update_user(self,user_id:int,update_data:Dict)-> None:
        pass