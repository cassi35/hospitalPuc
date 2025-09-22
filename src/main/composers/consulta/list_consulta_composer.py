from src.presentation.controllers.consulta.list_consulta_controller import ConsultaListController
from src.data.usecases.consulta.list_consulta import ConsultaListUseCase
from src.infra.db.repositories.consulta_repository import ConsultaRepository
def list_consulta_composer():
    repository = ConsultaRepository()
    usecase = ConsultaListUseCase(
        consulta_repository=repository
    )
    controller  = ConsultaListController(usecase=usecase)
    return controller.handle