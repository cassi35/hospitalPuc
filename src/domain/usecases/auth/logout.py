from abc import ABC, abstractmethod
from typing import Dict
class LogoutUseCase(ABC):
    @abstractmethod
    def logout(self, token: str) -> Dict:
        """Invalida token do usuário"""
        pass