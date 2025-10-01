from abc import ABC, abstractmethod
from typing import Dict
    
class ResendVerificationTokenUsecase(ABC):
    @abstractmethod
    def send_email(self, email: str, token: int) -> Dict:
        pass