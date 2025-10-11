from abc import ABC, abstractmethod
class GenerateVerification(ABC):
    @abstractmethod
    def generate(self,user_data:dict)->str:
        pass