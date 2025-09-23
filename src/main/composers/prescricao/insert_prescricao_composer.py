from src.presentation.controllers.prescricao.insert_prescricao_controller import PrescricaoInsertController
from src.data.usecases.prescricao.insert_prescricao import PrescricaoInsertUseCase
from src.infra.db.repositories.prescricao_repository import PrescricaoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def insert_prescricao_composer():
	prescricao_repository = PrescricaoRepository()
	paciente_repository = PacienteRepository()
	medico_repository = MedicoRepository()
	medicamento_repository = MedicamentoRepository()
	usecase = PrescricaoInsertUseCase(
		prescricao_repository=prescricao_repository,
		paciente_repository=paciente_repository,
		medico_repository=medico_repository,
		medicamento_repository=medicamento_repository,
	)
	controller = PrescricaoInsertController(usecase=usecase)
	return controller.handle
