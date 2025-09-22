from src.presentation.controllers.consulta.delete_consulta_controller import ConsultaDeleteController
from src.data.usecases.consulta.delete_consulta import ConsultaDeleteUseCase
from src.infra.db.repositories.consulta_repository import ConsultaRepository
def delete_consulta_composer():
    repository = ConsultaRepository()
    usecase = ConsultaDeleteUseCase(
        consulta_repository=repository
    )
    controller = ConsultaDeleteController(usecase=usecase)
    return controller.handle