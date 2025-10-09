from abc import ABC, abstractmethod
from typing import Dict
class TokenUseCase(ABC):
    @abstractmethod
    def verify(self, token: str) -> Dict:
        pass