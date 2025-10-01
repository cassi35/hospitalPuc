from abc import ABC, abstractmethod
from typing import Dict
    
class SendVerificationTokenUsecase(ABC):
    @abstractmethod
    def send_email(self, token:int, email:str) -> Dict:
        pass