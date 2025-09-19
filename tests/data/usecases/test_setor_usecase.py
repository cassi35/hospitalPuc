from src.data.interfaces.setor_interface_repository import SetorRepositoryInterface
from tests.infra.repositories.setor_repository_spy import SetorRepositorySpy
from src.domain.models.setor_model import Setor as SetorDomain
from src.data.usecases.setor.insert_setor import SetorInsertUseCase
from src.data.usecases.setor.delete_setor import SetorDeleteUseCase
from src.data.usecases.setor.update_setor import SetorUpdateUseCase
from src.data.usecases.setor.list_setor import SetorListUseCase
import pytest
setor_repository_spy = SetorRepositorySpy()
@pytest.mark.skip(reason='teste feito com sucesso')
def test_insert_setor_usecase():
    setor_insert_usecase = SetorInsertUseCase(setor_repository=setor_repository_spy)
    nome = 'dermatilogia'
    andar = 2
    capacidade = 10
    responsavel = 'cassiano2'
    setor = SetorDomain(
        id='1',
        nome=nome,
        andar=andar,
        capacidade=capacidade,
        responsavel=responsavel
    )
    response = setor_insert_usecase.insert(setor=setor)
    setor_response = response['attributes']
    print(response)
@pytest.mark.skip(reason="teste feito com sucesso")
def test_update_setor_usecase():
    setor_usecase_update = SetorUpdateUseCase(setor_repository=setor_repository_spy)
    nome = 'dermatilogia'
    andar = 2
    capacidade = 10
    responsavel = 'cassiano'
    setor = SetorDomain(
        id='1',
        nome=nome,
        andar=andar,
        capacidade=capacidade,
        responsavel=responsavel
    )
    response = setor_usecase_update.update(setor=setor,setor_id=1)
    setor_response = response['attributes']
    print(response)
@pytest.mark.skip(reason="teste feito com sucesso")
def test_delete_setor_usecase():
    setor_usecase_delete = SetorDeleteUseCase(setor_repository=setor_repository_spy)
    response = setor_usecase_delete.delete(setor_id=1)
    print(response)
@pytest.mark.skip(reason="teste feito com sucesso")
def test_list_setor_usecase():
    setor_usecase_list = SetorListUseCase(setor_repository=setor_repository_spy)
    response = setor_usecase_list.list()
    print(response)