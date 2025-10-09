from abc import ABC, abstractmethod
from typing import Dict

class ForgotPasswordUseCase(ABC):
    @abstractmethod
    def forgot_password(self, email: str) -> Dict:
        """Envia token de recuperação de senha"""
        pass