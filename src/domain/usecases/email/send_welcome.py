from abc import ABC, abstractmethod
from typing import Dict

class SendWelcomeEmailUsecase(ABC):
    @abstractmethod
    def send_email(self, email: str,name:str) -> Dict:
        pass