from abc import ABC, abstractmethod
from typing import Optional, Dict

class AuthCacheInterface(ABC):
    @abstractmethod
    def set(self,key:str,value:str) -> None:
        """Set auth cache"""
        pass
    @abstractmethod
    def get(self,key:str) -> Optional[str]:
        """Get auth cache"""
        pass
    @abstractmethod
    def delete(self,key:str) -> None:
        """Delete auth cache"""
        pass
    @abstractmethod
    def clear(self) -> None:
        """Clear all auth cache"""
        pass
