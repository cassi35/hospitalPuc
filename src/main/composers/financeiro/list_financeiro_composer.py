from src.presentation.controllers.financeiro.list_financeiro_controller import FinanceiroListController
from src.data.usecases.financeiro.list_financeiro import FinanceiroListUseCase
from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
def list_financeiro_composer():
    repository = FinanceiroRepository()
    usecase = FinanceiroListUseCase(
        financeiro_repository=repository
    )
    controller = FinanceiroListController(usecase=usecase)
    return controller.handle