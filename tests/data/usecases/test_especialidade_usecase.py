from tests.infra.repositories.especialidade_repository_spy import EspecialidadeRepositorySpy
from src.data.usecases.especialidade.insert_especialidade import EspecialidadeInsertUseCase
from src.data.usecases.especialidade.delete_especialidade import EspecialidadeDeleteUseCase
from src.data.usecases.especialidade.update_especialidade import EspecialidadeUpdateUseCase
from src.data.usecases.especialidade.list_especialidade import EspecialidadeListUseCase
from src.domain.models.especialidade_model import Especialidade as EspecialidadeDomain
import pytest
especialidade_repository_spy = EspecialidadeRepositorySpy()
@pytest.mark.skip(reason="concluido")
def test_insert_especialidade():
    especialidade_insert_usecase = EspecialidadeInsertUseCase(
        especialidade_repository=especialidade_repository_spy

    )
    especialidade = EspecialidadeDomain(
        descricao="Cardiologia",
        id=1,
        nome="Cardiologista"
    )
    response =  especialidade_insert_usecase.insert(
        especialidade=especialidade
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_update_especialidade():
    especialidade_update_usecase = EspecialidadeUpdateUseCase(
        especialidade_repository=especialidade_repository_spy
    )
    especialidade = EspecialidadeDomain(
        descricao="Cardiologia Atualizada",
        id=1,
        nome="Cardiologista Atualizado"
    )
    response =  especialidade_update_usecase.update(
        especialidade_id=1,
        especialidade=especialidade
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_delete_especialidade():
    especialidade_delete_usecase = EspecialidadeDeleteUseCase(
        especialidade_repository=especialidade_repository_spy
    )
    response =  especialidade_delete_usecase.delete(
        especialidade_id=1
    )
    print(response)
@pytest.mark.skip(reason="concluido")
def test_list_especialidade():
    especialidade_list_usecase = EspecialidadeListUseCase(
        especialidade_repository=especialidade_repository_spy
    )
    response =  especialidade_list_usecase.list()
    print(response)