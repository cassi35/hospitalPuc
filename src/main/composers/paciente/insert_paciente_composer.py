from src.presentation.controllers.paciente.insert_paciente_controller import PacienteInsertController
from src.data.usecases.paciente.insert_paciente import PacienteInsertUseCase
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.endereco_reposotory import EnderecoRepository
from src.infra.db.repositories.convenio_repository import ConvenioRepository

def insert_paciente_composer():
	paciente_repository = PacienteRepository()
	endereco_repository = EnderecoRepository()
	convenio_repository = ConvenioRepository()
	usecase = PacienteInsertUseCase(
		paciente_repository=paciente_repository,
		endereco_repository=endereco_repository,
		convenio_repository=convenio_repository
	)
	controller = PacienteInsertController(usecase=usecase)
	return controller.handle
