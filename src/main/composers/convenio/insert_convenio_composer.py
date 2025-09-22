from src.presentation.controllers.convenio.insert_convenio_controller import ConvenioInsertController
from src.data.usecases.convenio.insert_convenio import ConvenioInsertUseCase
from src.infra.db.repositories.convenio_repository import ConvenioRepository
def insert_convenio_composer():
    repository= ConvenioRepository()
    usecase = ConvenioInsertUseCase(
        convenio_repository=repository
    )
    controller = ConvenioInsertController(usecase=usecase)
    return controller.handle