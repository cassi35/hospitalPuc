from src.presentation.controllers.medicamento.delete_medicamento_controller import MedicamentoDeleteController
from src.data.usecases.medicamento.delete_medicamento import MedicamentoDeleteUseCase
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def delete_medicamento_composer():
	repository = MedicamentoRepository()
	usecase = MedicamentoDeleteUseCase(
		medicamento_repository=repository
	)
	controller = MedicamentoDeleteController(usecase=usecase)
	return controller.handle
