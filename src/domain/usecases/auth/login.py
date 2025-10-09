from abc import ABC, abstractmethod
from typing import Dict, Optional

class LoginUseCase(ABC):
    @abstractmethod
    def login(self, email: str, senha: str) -> Dict:
        """Autentica usuário e retorna token"""
        pass