from src.presentation.controllers.leito.list_leito_controller import LeitoListController
from src.data.usecases.leito.list_leito import LeitoListUseCase
from src.infra.db.repositories.leito_repository import LeitoRepository

def list_leito_composer():
	repository = LeitoRepository()
	usecase = LeitoListUseCase(
		leito_repository=repository
	)
	controller  = LeitoListController(usecase=usecase)
	return controller.handle
