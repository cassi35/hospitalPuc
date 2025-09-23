from src.presentation.controllers.paciente.delete_paciente_controller import PacienteDeleteController
from src.data.usecases.paciente.delete_paciente import PacienteDeleteUseCase
from src.infra.db.repositories.paciente_repository import PacienteRepository

def delete_paciente_composer():
	repository = PacienteRepository()
	usecase = PacienteDeleteUseCase(
		paciente_repository=repository
	)
	controller = PacienteDeleteController(usecase=usecase)
	return controller.handle
