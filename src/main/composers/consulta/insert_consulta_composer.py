from src.infra.db.repositories.consulta_repository import ConsultaRepository
from src.infra.db.repositories.paciente_repository import PacienteRepository
from src.infra.db.repositories.medico_repository import MedicoRepository
from src.infra.db.repositories.especialidade_repository import EspecialidadeRepository
from src.data.usecases.consulta.insert_consulta import ConsultaInsertUseCase

from src.presentation.controllers.consulta.insert_consulta_controller import ConsultaInsertController
def insert_consulta_composer():
    consulta_repository = ConsultaRepository()
    paciente_repository = PacienteRepository()
    medico_repository = MedicoRepository()
    especialidade_repository = EspecialidadeRepository()
    usecase = ConsultaInsertUseCase(
        consulta_repository=consulta_repository,
        paciente_repository=paciente_repository,
        medico_repository=medico_repository,
        especialidade_repository=especialidade_repository
    )
    controller = ConsultaInsertController(usecase=usecase)
    return controller.handle