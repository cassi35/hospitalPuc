from tests.infra.repositories.setor_repository_spy import SetorRepositorySpy
from tests.infra.repositories.funcionario_repository_spy import FuncionarioRepositorySpy
from src.data.usecases.funcionario.insert_funcionario import FuncionarioInsertUseCase
from src.data.usecases.funcionario.delete_funcionario import FuncionarioDeleteUseCase
from src.data.usecases.funcionario.update_funcionario import FuncionarioUpdateUseCase
from src.data.usecases.funcionario.list_funcionario import FuncionarioListUseCase
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain 
import pytest
stor_repository_spy = SetorRepositorySpy()
funcionario_repository_spy = FuncionarioRepositorySpy()
@pytest.mark.skip(reason="concluido")
def test_funcionario_insert():
    funcionario_insert_usecase = FuncionarioInsertUseCase(
        funcionario_repository=funcionario_repository_spy,
        setor_repository=stor_repository_spy 
    )
    nome = 'Carlos Silva'
    cargo = 'enfermeiro'
    setor_id = 1
    cpf = '12345678903'
    telefone = '123456789'
    email = 'carlos@hospital.com'
    data_contratacao="2023-10-01"
    funcionario = FuncionarioDomain(
        nome=nome,
        cargo=cargo,
        setor_id=setor_id,
        cpf=cpf,
        telefone=telefone,
        email=email,
        data_contratacao=data_contratacao,
        id=1 
    )
    response = funcionario_insert_usecase.insert(
        funcionario=funcionario
    )
    
    print(response)
@pytest.mark.skip(reason="concluido")
def test_funcionario_update():
    funcionario_update_usecase = FuncionarioUpdateUseCase(
        funcionario_repository=funcionario_repository_spy,
        setor_repository=stor_repository_spy 
    )
    id = 1
    nome = 'Carlos Silva'
    cargo = 'técnico'
    setor_id = 2
    cpf = '12345678903'
    telefone = '123456789'
    email = 'carlos.silva@hospital.com'
    data_contratacao="2023-10-01"
    funcionario = FuncionarioDomain(
        nome=nome,
        cargo=cargo,
        setor_id=setor_id,
        cpf=cpf,
        telefone=telefone,
        email=email,
        data_contratacao=data_contratacao,
        id=id 
    )
    response = funcionario_update_usecase.update(
        funcionario=funcionario,
        funcionario_id=id 
    )
    print(response)

@pytest.mark.skip(reason="concluido")
def test_funcionario_list():
    funcionario_list_usecase = FuncionarioListUseCase(
        funcionario_repository=funcionario_repository_spy
    )
    response = funcionario_list_usecase.list()
    print(response)

def test_delete_funcionario():
    funcionario_delete_usecase = FuncionarioDeleteUseCase(
        funcionario_repository=funcionario_repository_spy
    )
    response = funcionario_delete_usecase.delete(1)
    print(response)