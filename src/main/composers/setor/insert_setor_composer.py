from src.presentation.controllers.setor.insert_setor_controller import SetorInsertController
from src.data.usecases.setor.insert_setor import SetorInsertUseCase
from src.infra.db.repositories.setor_repository import SetorRepository

def insert_setor_composer():
	repository = SetorRepository()
	usecase = SetorInsertUseCase(
		setor_repository=repository
	)
	controller = SetorInsertController(usecase=usecase)
	return controller.handle
