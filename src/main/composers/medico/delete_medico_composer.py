from src.presentation.controllers.medico.delete_medico_controller import MedicoDeleteController
from src.data.usecases.medico.delete_medico import MedicoDeleteUseCase
from src.infra.db.repositories.medico_repository import MedicoRepository

def delete_medico_composer():
	repository = MedicoRepository()
	usecase = MedicoDeleteUseCase(
		medico_repository=repository
	)
	controller = MedicoDeleteController(usecase=usecase)
	return controller.handle
