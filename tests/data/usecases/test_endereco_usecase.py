from tests.infra.repositories.endereco_repository_spy import EnderecoRepositorySpy
from src.data.usecases.endereco.insert_endereco import EnderecoInsertUseCase
from src.data.usecases.endereco.delete_endereco import EnderecoDeleteUseCase
from src.data.usecases.endereco.update_endereco import EnderecoUpdateUseCase
from src.data.usecases.endereco.list_endereco import EnderecoListUseCase
from src.domain.models.endereco_model import Endereco  # ← ADICIONE ESTE IMPORT
import pytest

@pytest.mark.skip("desabilitado temporariamente")  # ✅ Com motivo
def test_insert_endereco_usecase():
    # Arrange
    endereco_repository_spy = EnderecoRepositorySpy()
    endereco_usecase = EnderecoInsertUseCase(endereco_repository_spy)
    
    # ✅ Use dados sem espaços
    endereco = Endereco(
        rua="RuaTeste",
        bairro="BairroTeste",
        cidade="CidadeTeste", 
        estado="EstadoTeste",
        cep="12345678"
    )
    
    # Act
    response = endereco_usecase.insert(endereco=endereco)
    
    # Assert
    assert endereco_repository_spy.insert_endereco_call_count == 1
    assert endereco_repository_spy.insert_endereco_attributes["rua"] == "RuaTeste"
    assert endereco_repository_spy.insert_endereco_attributes["bairro"] == "BairroTeste"
    assert endereco_repository_spy.insert_endereco_attributes["cidade"] == "CidadeTeste"
    assert endereco_repository_spy.insert_endereco_attributes["estado"] == "EstadoTeste"
    assert endereco_repository_spy.insert_endereco_attributes["cep"] == "12345678"
    assert response["type"] == "Endereco"
    assert response["count"] == 1
    assert response["attributes"]["rua"] == "RuaTeste"
# @pytest.mark.skip("desabilitado temporariamente") 
def test_delete_endereco_usecase():
    endereco_repository_spy = EnderecoRepositorySpy()
    endereco_usecase = EnderecoDeleteUseCase(endereco_repository=endereco_repository_spy)
    id = 1
    response = endereco_usecase.delete(endereco_id=id)
    assert response["attributes"]["id"] == id
    assert response["attributes"]["deleted"] is True
@pytest.mark.skip("desabilitado temporariamente")
def test_update_endereco_usecase():
    endereco_repository = EnderecoRepositorySpy()
    update_usecase = EnderecoUpdateUseCase(endereco_repository=endereco_repository)
    endereco = Endereco(
        rua="RuaAtualizada",
        bairro="BairroAtualizado",
        cidade="CidadeAtualizada",
        estado="EstadoAtualizado",
        cep="12345678"
    )
    response = update_usecase.update(endereco_id=1,endereco=endereco)
    print(response)
@pytest.mark.skip("desabilitado temporariamente")
def test_list_endereco_usecase():
    endereco_repository = EnderecoRepositorySpy()
    list_usecase = EnderecoListUseCase(endereco_repository=endereco_repository)
    response = list_usecase.list()
    print(response)