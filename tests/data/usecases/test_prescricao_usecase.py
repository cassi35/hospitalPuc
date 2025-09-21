from tests.infra.repositories.prescricao_repository_spy import  PrescricaoRepository as PrescricaoRepositorySpy
from tests.infra.repositories.medicamento_repository_spy import MedicamentoRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from src.data.usecases.prescricao.insert_prescricao import PrescricaoInsertUseCase
from src.data.usecases.prescricao.delete_prescricao import PrescricaoDeleteUseCase
from src.data.usecases.prescricao.update_prescricao import PrescricaoUpdateUseCase
from src.data.usecases.prescricao.list_prescricao import PrescricaoListUseCase
from src.domain.models.prescricao_model import Prescricao as PrescricaoDomain
import pytest
prescricacao_repository_spy = PrescricaoRepositorySpy()
medicamento_repository_spy = MedicamentoRepositorySpy()
paciente_repository_spy = PacienteRepositorySpy()
medico_repository_spy = MedicoRepositorySpy()
@pytest.mark.skip(reason='concluido teste')
def test_insert_prescricao():
    prescricao_insert_usecase = PrescricaoInsertUseCase(
        medicamento_repository=medicamento_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        prescricao_repository=prescricacao_repository_spy

    )
    paciente_id = 1
    medico_id = 1
    data_prescricao = '2025-09-02'
    medicamento_id = 1
    dosagem = 500
    frequencia = 3
    prescricao = PrescricaoDomain(
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_prescricao=data_prescricao,
        medicamento_id=medicamento_id,
        dosagem=dosagem,
        frequencia=frequencia,
        id=1
    )
    response = prescricao_insert_usecase.insert(
        prescricao=prescricao 
    )
    print(response)
@pytest.mark.skip(reason='concluido teste')
def test_update_prescricao(): 
    prescricao_update_usecase = PrescricaoUpdateUseCase(
        medicamento_repository=medicamento_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        prescricao_repository=prescricacao_repository_spy
    )
    paciente_id = 1
    medico_id = 2
    data_prescricao = '2025-09-03'
    medicamento_id = 2
    dosagem = 750
    frequencia = 2
    prescricao = PrescricaoDomain(
        paciente_id=paciente_id,
        medico_id=medico_id,
        data_prescricao=data_prescricao,
        medicamento_id=medicamento_id,
        dosagem=dosagem,
        frequencia=frequencia,
        id=1
    )
    response = prescricao_update_usecase.update(
        prescricao_id=1,
        prescricao=prescricao
    )
    print(response)
@pytest.mark.skip(reason='concluido teste')
def test_delete_prescricao(): 
    prescricao_delete_usecase = PrescricaoDeleteUseCase(
        prescricao_repository=prescricacao_repository_spy
    )
    response = prescricao_delete_usecase.delete(
        prescricao_id=1
    )
    print(response)
# @pytest.mark.skip(reason='concluido teste')
def test_list_prescricao(): 
    prescricao_list_usecase = PrescricaoListUseCase(
        prescricao_repository=prescricacao_repository_spy
    )
    response = prescricao_list_usecase.list()
    print(response)