from abc import ABC,abstractmethod
from typing import Dict
from src.domain.models.auth_model import AuthModel
class SignupUseCase(ABC):
    @abstractmethod
    def signup(self,auth:AuthModel)->Dict:
        """Signup usecase"""
        pass 