from src.presentation.controllers.prescricao.update_prescricao_controller import PrescricaoUpdateController
from src.data.usecases.prescricao.update_prescricao import PrescricaoUpdateUseCase
from src.infra.db.repositories.prescricao_repository import PrescricaoRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.medicamento_repository import MedicamentoRepository

def update_prescricao_composer():
	prescricao_repository = PrescricaoRepository()
	paciente_repository = PacienteRepository()
	medico_repository = MedicoRepository()
	medicamento_repository = MedicamentoRepository()
	usecase = PrescricaoUpdateUseCase(
		prescricao_repository=prescricao_repository,
		paciente_repository=paciente_repository,
		medico_repository=medico_repository,
		medicamento_repository=medicamento_repository,
	)
	controller = PrescricaoUpdateController(usecase=usecase)
	return controller.handle
