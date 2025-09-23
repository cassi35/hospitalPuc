from src.presentation.controllers.leito.update_leito_controller import LeitoUpdateController
from src.data.usecases.leito.update_leito import LeitoUpdateUseCase
from src.infra.db.repositories.leito_repository import LeitoRepository
from src.infra.db.repositories.setor_repository import SetorRepository

def update_leito_composer():
	leito_repository = LeitoRepository()
	setor_repository = SetorRepository()
	usecase = LeitoUpdateUseCase(
		leito_repository=leito_repository,
		setor_repository=setor_repository
	)
	controller = LeitoUpdateController(usecase=usecase)
	return controller.handle
