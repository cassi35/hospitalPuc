from src.presentation.controllers.setor.delete_setor_controller import SetorDeleteController
from src.data.usecases.setor.delete_setor import SetorDeleteUseCase
from src.infra.db.repositories.setor_repository import SetorRepository

def delete_setor_composer():
	repository = SetorRepository()
	usecase = SetorDeleteUseCase(
		setor_repository=repository
	)
	controller = SetorDeleteController(usecase=usecase)
	return controller.handle
