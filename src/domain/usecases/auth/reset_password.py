from abc import ABC, abstractmethod
from typing import Dict

class ResetPasswordUseCase(ABC):
    @abstractmethod
    def reset_password(self, email: str, token: str, nova_senha: str) -> Dict:
        """Redefine senha usando token"""
        pass