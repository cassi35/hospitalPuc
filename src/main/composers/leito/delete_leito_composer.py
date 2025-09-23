from src.presentation.controllers.leito.delete_leito_controller import LeitoDeleteController
from src.data.usecases.leito.delete_leito import LeitoDeleteUseCase
from src.infra.db.repositories.leito_repository import LeitoRepository

def delete_leito_composer():
	repository = LeitoRepository()
	usecase = LeitoDeleteUseCase(
		leito_repository=repository
	)
	controller = LeitoDeleteController(usecase=usecase)
	return controller.handle
