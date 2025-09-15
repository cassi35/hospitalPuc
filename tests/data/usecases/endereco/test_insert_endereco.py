from tests.infra.repositories.endereco_repository_spy import EnderecoRepositorySpy
from src.data.usecases.endereco.insert_endereco import EnderecoInsertUseCase
from src.infra.db.entities.endereco import Endereco  # ← ADICIONE ESTE IMPORT
import pytest

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