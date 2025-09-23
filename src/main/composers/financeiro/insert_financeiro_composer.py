from src.presentation.controllers.financeiro.insert_financeiro_controller import FinanceiroInsertController
from src.data.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase
from src.infra.db.repositories.financeiro_repository import FinanceiroRepository
from src.infra.db.repositories.convenio_repository import ConvenioRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.data.usecases.financeiro.insert_financeiro import FinanceiroInsertUseCase
def insert_financeiro_composer():
    financeiro_repository = FinanceiroRepository()
    convenio_repository = ConvenioRepository()
    paciente_repository = PacienteRepository()
    usecase = FinanceiroInsertUseCase(
        financeiro_repository=financeiro_repository,
        convenio_repository=convenio_repository,
        paciente_repository=paciente_repository
    )
    controller = FinanceiroInsertController(usecase=usecase)
    return controller.handle