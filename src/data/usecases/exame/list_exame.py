from typing import List, Dict
from src.domain.usecases.exame.list_exame import ExameListUseCase as ExameListInterface
from src.data.interfaces.exame_interface_repository import ExameRepositoryInterface
from src.domain.models.exame_model import Exame  # apenas para type hints

class ExameListUseCase(ExameListInterface):
    def __init__(self, exame_repository: ExameRepositoryInterface):
        self.exame_repository = exame_repository

    def list(self) -> List[Dict]:
        exames = self.exame_repository.findAll()
        return [self.__format_response(exame) for exame in exames]

    def __format_response(self, exame: Exame) -> Dict:
        response = {
            "type": "Exame",
            "id": exame.id,
            "attributes": {
                "tipo_exame": exame.tipo_exame,
                "data_exame": exame.data_exame.isoformat() if exame.data_exame else None,
                "paciente_id": exame.paciente_id,
                "medico_id": exame.medico_id,
                "resultado": exame.resultado,
                "status": exame.status
            }
        }
        return response