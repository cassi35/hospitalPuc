from src.presentation.controllers.medico.list_medico_controller import MedicoListController
from src.data.usecases.medico.list_medico import MedicoListUseCase
from src.infra.db.repositories.medico_repository import MedicoRepository

def list_medico_composer():
	repository = MedicoRepository()
	usecase = MedicoListUseCase(
		medico_repository=repository
	)
	controller = MedicoListController(usecase=usecase)
	return controller.handle
