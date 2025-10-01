from abc import ABC, abstractmethod
from typing import Dict
    
class ResetPasswordEmailUsecase(ABC):
    @abstractmethod
    def send_email(self, email: str) -> Dict:
        pass