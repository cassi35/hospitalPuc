from src.presentation.controllers.convenio.update_convenio_controller import ConvenioUpdateController
from src.data.usecases.convenio.update_convenio import ConvenioUpdateUseCase
from src.infra.db.repositories.convenio_repository import ConvenioRepository
def update_convenio_composer():
    repository = ConvenioRepository()
    usecase = ConvenioUpdateUseCase(
        convenio_repository=repository
    )
    controller = ConvenioUpdateController(usecase=usecase)
    return controller.handle