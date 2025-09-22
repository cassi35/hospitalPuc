from src.infra.db.repositories.convenio_repository import ConvenioRepository
from src.data.usecases.convenio.list_convenio import ConvenioListUseCase
from src.presentation.controllers.convenio.list_convenio_controller import ConvenioListController
def list_convenio_composer():
    repository = ConvenioRepository()
    usecase = ConvenioListUseCase(
        convenio_repository=repository
    )
    controller = ConvenioListController(usecase=usecase)
    return controller.handle