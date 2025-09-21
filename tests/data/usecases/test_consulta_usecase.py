from tests.infra.repositories.consulta_repository_spy import ConsultaRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from tests.infra.repositories.especialidade_repository_spy import EspecialidadeRepositorySpy
from src.data.usecases.consulta.insert_consulta import ConsultaInsertUseCase
from src.data.usecases.consulta.delete_consulta import ConsultaDeleteUseCase
from src.data.usecases.consulta.update_consulta import ConsultaUpdateUseCase
from src.data.usecases.consulta.list_consulta import ConsultaListUseCase
from src.domain.models.consulta_model import Consulta as ConsultaDomain
import pytest

consulta_repository_spy = ConsultaRepositorySpy()
paciente_repository_spy = PacienteRepositorySpy()
medico_repository_spy = MedicoRepositorySpy()
especialidade_repository_spy = EspecialidadeRepositorySpy()

@pytest.mark.skip(reason="concluido")
def test_insert_consulta():
    consulta_insert_usecase = ConsultaInsertUseCase(
        consulta_repository=consulta_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        especialidade_repository=especialidade_repository_spy
    )
    consulta = ConsultaDomain(
        id=1,
        data_hora="2025-12-01",
        paciente_id=1,
        medico_id=1,
        especialidade_id=1,
        status="ativo",
        observacoes="Consulta teste"
    )
    response = consulta_insert_usecase.insert(consulta=consulta)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_delete_consulta():
    consulta_delete_usecase = ConsultaDeleteUseCase(
        consulta_repository=consulta_repository_spy
    )
    response = consulta_delete_usecase.delete(1)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_update_consulta():
    consulta_update_usecase = ConsultaUpdateUseCase(
        consulta_repository=consulta_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        especialidade_repository=especialidade_repository_spy
    )
    consulta = ConsultaDomain(
        id=1,
        data_hora="2025-12-01",
        paciente_id=1,
        medico_id=1,
        especialidade_id=1,
        status="ativo",
        observacoes="Consulta atualizada"
    )
    response = consulta_update_usecase.update(consulta_id=1, consulta=consulta)
    print(response)

# @pytest.mark.skip(reason="concluido")
def test_list_consulta():
    consulta_list_usecase = ConsultaListUseCase(
        consulta_repository=consulta_repository_spy
    )
    response = consulta_list_usecase.list()
    print(response)