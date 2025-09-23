from src.presentation.controllers.setor.update_setor_controller import SetorUpdateController
from src.data.usecases.setor.update_setor import SetorUpdateUseCase
from src.infra.db.repositories.setor_repository import SetorRepository

def update_setor_composer():
	repository = SetorRepository()
	usecase = SetorUpdateUseCase(
		setor_repository=repository
	)
	controller = SetorUpdateController(usecase=usecase)
	return controller.handle
