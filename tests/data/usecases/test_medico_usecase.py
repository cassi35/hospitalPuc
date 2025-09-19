from tests.infra.repositories.especialidade_repository_spy import EspecialidadeRepositorySpy
from tests.infra.repositories.medico_repository_spy import MedicoRepositorySpy
from src.data.usecases.medico.insert_medico import MedicoInsertUseCase
from src.data.usecases.medico.delete_medico import MedicoDeleteUseCase
from src.data.usecases.medico.update_medico import MedicoUpdateUseCase
from src.data.usecases.medico.list_medico import MedicoListUseCase
from src.domain.models.medico_model import Medico as MedicoDomain
import pytest
especialidade_repository_spy = EspecialidadeRepositorySpy()
medico_repository_spy = MedicoRepositorySpy()
@pytest.mark.skip(reason="teste completo com sucessos")
def test_insert_medico():
    medico_insert_usecase = MedicoInsertUseCase(
        medico_repository_spy, especialidade_repository_spy
    )
    nome = 'cassiano'
    cpf = '12345678901'
    especialidade_id = 2
    telefone = '119999993'
    email = 'cassiano@gmail.com'
    status = 'ativo'
    medico = MedicoDomain(
        id=1,
        nome=nome,
        cpf=cpf,
        especialidade_id=especialidade_id,
        telefone=telefone,
        email=email,
        status=status,
    )
    response = medico_insert_usecase.insert(
        medico=medico
    )
    print(response)
@pytest.mark.skip(reason="teste completo com sucessos")
def test_update_medico_usecase():
    medico_update_usecase = MedicoUpdateUseCase(
        especialidade_repository=especialidade_repository_spy,
        medico_repository=medico_repository_spy
    )
    nome = 'cassiano'
    cpf = '12345678901'
    especialidade_id = 3
    telefone = '119999993'
    email = 'cassiano@gmail.com'
    status = 'ativo'
    medico = MedicoDomain(
        id=1,
        nome=nome,
        cpf=cpf,
        especialidade_id=especialidade_id,
        telefone=telefone,
        email=email,
        status=status
    )
    response = medico_update_usecase.update(
        medico=medico,
        medico_id=1
    )
    print(response)
@pytest.mark.skip(reason="teste completo com sucessos")
def test_delete_medico_usecase():
    medico_delete_usecase = MedicoDeleteUseCase(
        medico_repository=medico_repository_spy
    )
    response = medico_delete_usecase.delete(
        medico_id=2
    )
    print(response)
@pytest.mark.skip(reason="teste completo com sucessos")
def test_list_medico_usecase():
    medico_list_usecase = MedicoListUseCase(
        medico_repository=medico_repository_spy
    )
    response = medico_list_usecase.list()
    print(response)