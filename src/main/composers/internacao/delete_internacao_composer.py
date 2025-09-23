from src.presentation.controllers.internacao.delete_internacao_controller import InternacaoDeleteController
from src.data.usecases.internacao.delete_internacao import InternacaoDeleteUseCase
from src.infra.db.repositories.internacao_repository import InternacaoRepository
def delete_internacao_composer():
    repository = InternacaoRepository()
    usecase = InternacaoDeleteUseCase(
        internacao_repository=repository
    )
    controller = InternacaoDeleteController(usecase=usecase)
    return controller.handle