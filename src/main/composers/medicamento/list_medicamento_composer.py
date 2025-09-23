from src.presentation.controllers.medicamento.list_medicamento_controller import MedicamentoListController
from src.data.usecases.medicamento.list_medicamento import MedicamentoListUseCase
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def list_medicamento_composer():
	repository = MedicamentoRepository()
	usecase = MedicamentoListUseCase(
		medicamento_repository=repository
	)
	controller  = MedicamentoListController(usecase=usecase)
	return controller.handle
