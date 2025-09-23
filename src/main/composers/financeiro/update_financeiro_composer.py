from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
from src.infra.db.repositories.convenio_repository import ConvenioRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.presentation.controllers.financeiro.update_financeiro_controller import FinanceiroUpdateController
from src.data.usecases.financeiro.update_financeiro import FinanceiroUpdateUseCase
def update_financeiro_composer():
    financeiro_repository = FinanceiroRepository()
    convenio_repository = ConvenioRepository()
    paciente_repository = PacienteRepository()
    usecase = FinanceiroUpdateUseCase(
        financeiro_repository=financeiro_repository,
        convenio_repository=convenio_repository,
        paciente_repository=paciente_repository
    )
    controller = FinanceiroUpdateController(usecase=usecase)
    return controller.handle