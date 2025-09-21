from tests.infra.repositories.leito_repository_spy import LeitoRepositorySpy
from src.data.usecases.leito.insert_leito import LeitoInsertUseCase
from src.data.usecases.leito.delete_leito import LeitoDeleteUseCase
from src.data.usecases.leito.update_leito import LeitoUpdateUseCase
from src.data.usecases.leito.list_leito import LeitoListUseCase
from src.domain.models.leito_model import Leito as LeitoDomain 
from tests.infra.repositories.setor_repository_spy import SetorRepositorySpy
import pytest 
leito_repository_spy = LeitoRepositorySpy()
setor_repository_spy = SetorRepositorySpy()
@pytest.mark.skip(reason="concluido")
def test_insert_leito():
    leito_insert_usecase = LeitoInsertUseCase(
leito_repository=leito_repository_spy,
setor_repository=setor_repository_spy
    )
    leito = LeitoDomain(
        numero_leito=3,
        setor_id=1,
        tipo='Enfermaria',
        status='disponivel',
        id=2
    )
    response = leito_insert_usecase.insert(
        leito=leito
    )
    print(response)
@pytest.mark.skip(reason="concluido")

def test_delete_leito():
    leito_delete_usecase = LeitoDeleteUseCase(
        leito_repository=leito_repository_spy
    )
    response = leito_delete_usecase.delete(1)
    print(response)
@pytest.mark.skip(reason="concluido")
def test_update_leito():
    leito_update_usecase = LeitoUpdateUseCase(
        leito_repository=leito_repository_spy,
        setor_repository=setor_repository_spy
    )
    leito = LeitoDomain(
        numero_leito=3,
        setor_id=1,
        tipo='Enfermaria',
        status='disponivel',
        id=2
    )
    response = leito_update_usecase.update(
        leito=leito,
        leito_id=2
    )
    print(response)
def test_list_leito():
    leito_list_usecase = LeitoListUseCase(
        leito_repository=leito_repository_spy
    )
    response = leito_list_usecase.list()
    print(response)