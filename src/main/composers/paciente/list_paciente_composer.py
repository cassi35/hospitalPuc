from src.presentation.controllers.paciente.list_paciente_controller import PacienteListController
from src.data.usecases.paciente.list_paciente import PacienteListUseCase
from src.infra.db.repositories.paciente_repository import PacienteRepository

def list_paciente_composer():
	repository = PacienteRepository()
	usecase = PacienteListUseCase(
		paciente_repository=repository
	)
	controller  = PacienteListController(usecase=usecase)
	return controller.handle
