from abc import ABC, abstractmethod
from typing import Dict

class VerifyEmailUseCase(ABC):
    @abstractmethod
    def verify(self, email: str, token: str) -> Dict:
        """Verifica token de email"""
        pass