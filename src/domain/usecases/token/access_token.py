from abc import ABC, abstractmethod
from typing import Dict
class AccessTokenUsecase(ABC):
    @abstractmethod
    def verify_access(self, token: str) -> Dict:
        pass