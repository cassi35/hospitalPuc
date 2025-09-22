from typing import List, Dict
from src.domain.usecases.convenio.list_convenio import ConvenioListUseCase as ConvenioListInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.domain.models.convenio_model import Convenio
class ConvenioListUseCase(ConvenioListInterface):
    def __init__(self, convenio_repository: ConvenioRepositoryInterface):
        self.convenio_repository = convenio_repository
    
    def list(self) -> List[Dict]:
        convenios = self.convenio_repository.findAll()
        return [self.__format__response(convenio) for convenio in convenios]
    def __format__response(self,convenio:Convenio)-> Dict:
        return  {
            "type":"Convenio",
            "id":convenio.id,
            "attributes":{
                "nome":convenio.nome,
                "tipo_plano":convenio.tipo_plano
            }
        } 