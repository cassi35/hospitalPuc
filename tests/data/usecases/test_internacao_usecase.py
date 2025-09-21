from tests.infra.repositories.internacao_repository_spy import InternacaoRepositorySpy
from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from tests.infra.repositories.leito_repository_spy import LeitoRepositorySpy
from src.data.usecases.internacao.insert_internacao import InternacaoInsertUseCase
from src.data.usecases.internacao.delete_internacao import InternacaoDeleteUseCase
from src.data.usecases.internacao.update_internacao import InternacaoUpdateUseCase
from src.data.usecases.internacao.list_internacao import InternacaoListUseCase
from src.domain.models.internacao_model import Internacao as InternacaoDomain
import pytest
internacao_repository_spy = InternacaoRepositorySpy()
paciente_repository_spy = PacienteRepositorySpy()
medico_repository_spy = MedicoRepositorySpy()
leito_repository_spy = LeitoRepositorySpy()
@pytest.mark.skip(reason="concluido")
def test_insert_internacao():
    internacao_insert_usecase = InternacaoInsertUseCase(
        internacao_repository=internacao_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        leito_repository=leito_repository_spy 
    )
    paciente_id = 1
    medico_id = 1
    leito_id = 1
    status = 'alta'    
    data_entrada = '2025-09-01'
    internacao = InternacaoDomain(
        paciente_id=paciente_id,
        medico_id=medico_id,
        leito_id=leito_id,
        data_entrada=data_entrada,
        id=1,
        status=status,
    )
    response = internacao_insert_usecase.insert(
        internacao=internacao
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_update_internacao():
    internacao_update_usecase = InternacaoUpdateUseCase(
        internacao_repository=internacao_repository_spy,
        paciente_repository=paciente_repository_spy,
        medico_repository=medico_repository_spy,
        leito_repository=leito_repository_spy 
    )
    id = 1
    paciente_id = 1
    medico_id = 2
    leito_id = 2
    status = 'alta'
    data_entrada = '2025-09-01'
    internacao = InternacaoDomain(
        id=id,
        paciente_id=paciente_id,
        medico_id=medico_id,
        leito_id=leito_id,
        data_entrada=data_entrada,
        status=status
    )
    response = internacao_update_usecase.update(
        internacao=internacao,
        internacao_id=id
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_delete_internacao():
    internacao_usecase_delete = InternacaoDeleteUseCase(
        internacao_repository=internacao_repository_spy
    )
    id = 2
    response = internacao_usecase_delete.delete(
        internacao_id=id
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_list_internacao():
    internacao_list_usecase = InternacaoListUseCase(
        internacao_repository=internacao_repository_spy
    )
    response = internacao_list_usecase.list()
    print(response)