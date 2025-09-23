from src.presentation.controllers.internacao.list_internacao_controller import InternacaoListController
from src.data.usecases.internacao.list_internacao import InternacaoListUseCase
from src.infra.db.repositories.internacao_repository import InternacaoRepository
def list_internacao_composer():
    repository = InternacaoRepository()
    usecase = InternacaoListUseCase(
        internacao_repository=repository
    )
    controller = InternacaoListController(usecase=usecase)
    return controller.handle