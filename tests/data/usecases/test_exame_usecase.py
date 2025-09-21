from tests.infra.repositories.exame_repository_spy import ExameRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from src.data.usecases.exame.insert_exame import ExameInsertUseCase
from src.data.usecases.exame.delete_exame import ExameDeleteUseCase
from src.data.usecases.exame.update_exame import ExameUpdateUseCase
from src.data.usecases.exame.list_exame import ExameListUseCase
from src.domain.models.exame_model import Exame as ExameDomain
import pytest

exame_repository_spy = ExameRepositorySpy()
paciente_repository_spy = PacienteRepositorySpy()
medico_repository_spy = MedicoRepositorySpy()

@pytest.mark.skip(reason="concluido")
def test_insert_exame():
    exame_insert_usecase = ExameInsertUseCase(
        exame_repository=exame_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy
    )
    exame = ExameDomain(
        id=1,
        tipo_exame="Hemograma",
        data_exame="2024-01-01",
        paciente_id=1,
        medico_id=1,
        resultado="Normal",
        status="concluído"
    )
    response = exame_insert_usecase.insert(exame=exame)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_delete_exame():
    exame_delete_usecase = ExameDeleteUseCase(
        exame_repository=exame_repository_spy
    )
    response = exame_delete_usecase.delete(1)
    print(response)

# @pytest.mark.skip(reason="concluido")
def test_update_exame():
    exame_update_usecase = ExameUpdateUseCase(
        exame_repository=exame_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy
    )
    exame = ExameDomain(
        id=1,
        tipo_exame="Hemograma Completo",
        data_exame="2024-01-01",
        paciente_id=1,
        medico_id=1,
        resultado="Alterado",
        status="concluído"
    )
    response = exame_update_usecase.update(exame_id=1, exame=exame)
    print(response)

@pytest.mark.skip(reason="concluido")
def test_list_exame():
    exame_list_usecase = ExameListUseCase(
        exame_repository=exame_repository_spy
    )
    response = exame_list_usecase.list()
    print(response)