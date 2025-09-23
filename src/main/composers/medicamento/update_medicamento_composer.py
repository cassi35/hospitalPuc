from src.presentation.controllers.medicamento.update_medicamento_controller import MedicamentoUpdateController
from src.data.usecases.medicamento.update_medicamento import MedicamentoUpdateUseCase
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def update_medicamento_composer():
	repository = MedicamentoRepository()
	usecase = MedicamentoUpdateUseCase(
		medicamento_repository=repository
	)
	controller = MedicamentoUpdateController(usecase=usecase)
	return controller.handle
