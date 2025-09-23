from src.presentation.controllers.medico.insert_medico_controller import MedicoInsertController
from src.data.usecases.medico.insert_medico import MedicoInsertUseCase
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository

def insert_medico_composer():
	medico_repository = MedicoRepository()
	especialidade_repository = EspecialidadeRepository()
	usecase = MedicoInsertUseCase(
		medico_repository=medico_repository,
		especialidade_repository=especialidade_repository
	)
	controller = MedicoInsertController(usecase=usecase)
	return controller.handle
