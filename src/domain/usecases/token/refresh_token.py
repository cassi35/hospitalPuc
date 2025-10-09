from abc import ABC, abstractmethod
from typing import Dict
class RefreshTokenUsecase(ABC):
    @abstractmethod
    def verify_refresh(self, token: str) -> Dict:
        pass