from src.presentation.controllers.medico.update_medico_controller import MedicoUpdateController
from src.data.usecases.medico.update_medico import MedicoUpdateUseCase
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository

def update_medico_composer():
	medico_repository = MedicoRepository()
	especialidade_repository = EspecialidadeRepository()
	usecase = MedicoUpdateUseCase(
		medico_repository=medico_repository,
		especialidade_repository=especialidade_repository
	)
	controller = MedicoUpdateController(usecase=usecase)
	return controller.handle
