from src.presentation.controllers.paciente.update_paciente_controller import PacienteUpdateController
from src.data.usecases.paciente.update_paciente import PacienteUpdateUseCase
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
from src.infra.db.repositories.convenio_repository import ConvenioRepository

def update_paciente_composer():
	paciente_repository = PacienteRepository()
	endereco_repository = EnderecoRepository()
	convenio_repository = ConvenioRepository()
	usecase = PacienteUpdateUseCase(
		paciente_repository=paciente_repository,
		endereco_repository=endereco_repository,
		convenio_repository=convenio_repository
	)
	controller = PacienteUpdateController(usecase=usecase)
	return controller.handle
