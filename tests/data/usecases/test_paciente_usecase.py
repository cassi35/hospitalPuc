from tests.infra.repositories.paciente_repository_spy import PacienteRepositorySpy
from tests.infra.repositories.endereco_repository_spy import EnderecoRepositorySpy
from tests.infra.repositories.convenio_repository_spy import ConvenioRepositorySpy
from src.data.usecases.paciente.insert_paciente import PacienteInsertUseCase
from src.data.usecases.paciente.delete_paciente import PacienteDeleteUseCase
from src.data.usecases.paciente.update_paciente import PacienteUpdateUseCase
from src.data.usecases.paciente.list_paciente import PacienteListUseCase
from src.domain.models.paciente_model import Paciente as PacienteDomain

import pytest
paciente_repository = PacienteRepositorySpy()
endereco_repository = EnderecoRepositorySpy()
convenio_repository = ConvenioRepositorySpy()
@pytest.mark.skip(reason="teste criando com sucesso")
def test_insert_paciente_usecase():
    paciente_insert = PacienteInsertUseCase(
        paciente_repository=paciente_repository,
        endereco_repository=endereco_repository,
        convenio_repository=convenio_repository
    )
    nome = 'teste'
    cpf = '12345678903'
    data_nascimento = '1990-01-01'
    sexo = 'm'
    telefone = '12345678903'
    alergia = 'nenhuma'
    contato_emergencia = '12345678903'
    endereco_id = 13
    convenio_id = 1
    paciente = PacienteDomain(
        id=1,
        nome=nome,
        cpf=cpf,
        data_nascimento=data_nascimento,
        sexo=sexo,
        telefone=telefone,
        alergia=alergia,
        contato_emergencia=contato_emergencia,
        endereco_id=endereco_id,
        convenio_id=convenio_id
    )
    
    response = paciente_insert.insert(
        paciente=paciente
    )
    print(response)