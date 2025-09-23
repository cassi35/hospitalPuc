from src.presentation.controllers.leito.insert_leito_controller import LeitoInsertController
from src.data.usecases.leito.insert_leito import LeitoInsertUseCase
from src.infra.db.repositories.leito_repository import LeitoRepository
from src.infra.db.repositories.setor_repository import SetorRepository
def insert_leito_composer():
    leito_repository = LeitoRepository()
    setor_repository = SetorRepository()
    usecase = LeitoInsertUseCase(
        leito_repository=leito_repository,
        setor_repository=setor_repository
    )
    controller = LeitoInsertController(usecase=usecase)
    return controller.handle