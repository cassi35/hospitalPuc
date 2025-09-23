from src.presentation.controllers.financeiro.delete_financeiro_controller import FinanceiroDeleteController
from src.data.usecases.financeiro.delete_financeiro import FinanceiroDeleteUseCase
from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
def delete_financeiro_composer():
    repository = FinanceiroRepository()
    usecase = FinanceiroDeleteUseCase(
        financeiro_repository=repository
    )
    controller = FinanceiroDeleteController(usecase=usecase)
    return controller.handle