from abc import ABC,abstractmethod
class URSafeTokenServiceInterface(ABC):
    @abstractmethod
    def create_url_safe_token(self,data:dict)->str:
        pass
    @abstractmethod
    def decode_url_safe_token(self,token:str)->dict:
        pass