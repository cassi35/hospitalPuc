from src.presentation.controllers.setor.list_setor_controller import SetorListController
from src.data.usecases.setor.list_setor import SetorListUseCase
from src.infra.db.repositories.setor_repository import SetorRepository

def list_setor_composer():
	repository = SetorRepository()
	usecase = SetorListUseCase(
		setor_repository=repository
	)
	controller = SetorListController(usecase=usecase)
	return controller.handle
