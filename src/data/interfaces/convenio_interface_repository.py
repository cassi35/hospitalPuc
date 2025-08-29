from abc import ABC,abstractmethod
from src.domain.models.convenio_model import Convenio
class ConvenioRepositoryInterface(ABC):
     @abstractmethod
     def insert_convenio(self,nome:str,tipo_plano:str)->None:pass 
     @abstractmethod
     def delete_convenio(self,id:int)->bool:pass 
     @abstractmethod
     def select_convenio(self,id:int)->Convenio:pass 
     @abstractmethod
     def udpate_convenio(self,id:int,nome:str,tipo_plano:str)->None:pass 
