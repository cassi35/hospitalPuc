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
            "id": getattr(exame, "id", None),
            "attributes": {
                "tipo_exame": getattr(exame, "tipo_exame", None),
                "data_exame": getattr(exame, "data_exame", None),
                "paciente_id": getattr(exame, "paciente_id", None),
                "medico_id": getattr(exame, "medico_id", None),
                "resultado": getattr(exame, "resultado", None),
                "status": getattr(exame, "status", None)
            }
        }
        return response