from tests.infra.repositories.convenio_repository_spy import ConvenioRepositorySpy
from src.data.usecases.convenio.insert_convenio import ConvenioInsertUseCase
from src.data.usecases.convenio.delete_convenio import ConvenioDeleteUseCase
from src.data.usecases.convenio.update_convenio import ConvenioUpdateUseCase
from src.data.usecases.convenio.list_convenio import ConvenioListUseCase
from src.domain.models.convenio_model import Convenio as ConvenioDomain
import pytest
convenio_repository = ConvenioRepositorySpy()

def test_insert_convenio_usecase():
    convenio_insert = ConvenioInsertUseCase(convenio_repository)
    convenio = ConvenioDomain(
        id=1,
        nome="ipsaude",
        tipo_plano="Empresarial"
    )
    response = convenio_insert.insert(convenio=convenio)
    print(response)