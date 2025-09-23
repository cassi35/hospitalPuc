from src.presentation.controllers.medicamento.insert_medicamento_controller import MedicamentoInsertController
from src.data.usecases.medicamento.insert_medicamento import MedicamentoInsertUseCase
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def insert_medicamento_composer():
	repository = MedicamentoRepository()
	usecase = MedicamentoInsertUseCase(
		medicamento_repository=repository
	)
	controller = MedicamentoInsertController(usecase=usecase)
	return controller.handle
