from src.presentation.controllers.convenio.delete_convenio_controller import ConvenioDeleteController
from src.data.usecases.convenio.delete_convenio import ConvenioDeleteUseCase
from src.infra.db.repositories.convenio_repository import ConvenioRepository
def delete_convenio_composer():
    repository = ConvenioRepository()
    usecase = ConvenioDeleteUseCase(
        convenio_repository=repository
    )
    controller = ConvenioDeleteController(usecase=usecase)
    return controller.handle