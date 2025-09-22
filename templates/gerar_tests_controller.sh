#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.."; pwd)"
TEST_CTRL_DIR="$ROOT_DIR/tests/presentation/controllers"

echo "Gerando tests de controllers (exceto endereco e convenio) em: $TEST_CTRL_DIR"
echo ""

declare -A BODY_JSON

# Amostras por entidade (compatíveis com seu SQL)
BODY_JSON[consulta]='{
            "data_hora": "2025-09-01",
            "paciente_id": 1,
            "medico_id": 1,
            "especialidade_id": 1,
            "status": "ativo",
            "observacoes": "Retorno"
        }'

BODY_JSON[especialidade]='{
            "nome": "Cardiologia",
            "descricao": "Coração e vasos"
        }'

BODY_JSON[exame]='{
            "tipo_exame": "Hemograma",
            "data_exame": "2025-09-01",
            "paciente_id": 1,
            "medico_id": 1,
            "resultado": "Normal",
            "status": "solicitado"
        }'

BODY_JSON[financeiro]='{
            "paciente_id": 1,
            "convenio_id": 1,
            "valor": 100.0,
            "data_emisao": "2025-09-01",
            "data_vencimento": "2025-09-10",
            "status_pagamento": "pendente"
        }'

BODY_JSON[funcionario]='{
            "nome": "João Silva",
            "cpf": "12345678901",
            "cargo": "enfermeiro",
            "setor_id": 1,
            "telefone": "999999999",
            "email": "joao@exemplo.com",
            "data_contratacao": "2025-09-01"
        }'

BODY_JSON[internacao]='{
            "paciente_id": 1,
            "medico_id": 1,
            "leito_id": 1,
            "data_entrada": "2025-09-01",
            "status": "em andamento"
        }'

BODY_JSON[leito]='{
            "numero_leito": "A101",
            "setor_id": 1,
            "tipo": "Enfermaria",
            "status": "disponivel"
        }'

BODY_JSON[medicamento]='{
            "nome": "Dipirona",
            "descricao": "Analgésico",
            "fabricante": "Farmaco SA",
            "validade": "2026-12-31",
            "quantidade_estoque": 50
        }'

BODY_JSON[medico]='{
            "nome": "Dra Ana",
            "cpf": "98765432100",
            "especialidade_id": 1,
            "telefone": "888888888",
            "email": "ana@exemplo.com",
            "status": "ativo"
        }'

BODY_JSON[paciente]='{
            "nome": "Carlos",
            "cpf": "11122233344",
            "data_nascimento": "1990-01-01",
            "sexo": "m",
            "telefone": "99988877766",
            "contato_emergencia": "99887766554",
            "alergia": "Nenhuma",
            "endereco_id": 1,
            "convenio_id": 1
        }'

BODY_JSON[prescricao]='{
            "paciente_id": 1,
            "medico_id": 1,
            "data_prescricao": "2025-09-01",
            "medicamento_id": 1,
            "dosagem": 1,
            "frequencia": 8
        }'

BODY_JSON[setor]='{
            "nome": "UTI Adulto",
            "andar": 2,
            "capacidade": 10,
            "responsavel": "Carlos"
        }'

# Itera pelas pastas de controllers de teste já existentes
shopt -s nullglob
for entity_dir in "$TEST_CTRL_DIR"/*/; do
  entity="$(basename "$entity_dir")"
  [[ "$entity" == "__pycache__" ]] && continue
  [[ "$entity" == "endereco" ]] && { echo "• Pulando endereco (não será alterado)"; echo ""; continue; }
  [[ "$entity" == "convenio" ]] && { echo "• Pulando convenio (não será alterado)"; echo ""; continue; }

  # Se não houver sample para a entidade, pula
  if [[ -z "${BODY_JSON[$entity]+x}" ]]; then
    echo "• Sem sample configurado para: $entity (pulado)"
    echo ""
    continue
  fi

  EntityCap="$(echo "$entity" | sed 's/.*/\u&/')"

  mkdir -p "$entity_dir"

  # INSERT
  cat > "$entity_dir/test_insert_${entity}_controller.py" <<EOF
from src.presentation.controllers.${entity}.insert_${entity}_controller import ${EntityCap}InsertController
from tests.data.mock.${entity}.insert_${entity}_spy import ${EntityCap}InsertUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self) -> None:
        self.body = ${BODY_JSON[$entity]}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ${EntityCap}InsertUsecaseSpy()
    controller = ${EntityCap}InsertController(usecase_spy)
    response = controller.handle(http_request=http_request_mock)
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
EOF

  # UPDATE
  cat > "$entity_dir/test_update_${entity}_controller.py" <<EOF
from tests.data.mock.${entity}.update_${entity}_spy import ${EntityCap}UpdateUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.controllers.${entity}.update_${entity}_controller import ${EntityCap}UpdateController
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
        self.body = ${BODY_JSON[$entity]}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ${EntityCap}UpdateUsecaseSpy()
    controller = ${EntityCap}UpdateController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
EOF

  # DELETE
  cat > "$entity_dir/test_delete_${entity}_controller.py" <<EOF
from src.presentation.controllers.${entity}.delete_${entity}_controller import ${EntityCap}DeleteController
from tests.data.mock.${entity}.delete_${entity}_spy import ${EntityCap}DeleteUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        self.path_params = {"id": 2}
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ${EntityCap}DeleteUsecaseSpy()
    controller = ${EntityCap}DeleteController(usecase_spy)
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
    assert response.status_code == 200 
    assert response.body["type"] is not None
EOF

  # LIST
  cat > "$entity_dir/test_list_${entity}_controller.py" <<EOF
from src.presentation.controllers.${entity}.list_${entity}_controller import ${EntityCap}ListController
from tests.data.mock.${entity}.list_${entity}_spy import ${EntityCap}ListUsecaseSpy
from src.presentation.http_types.http_response import HTTPResponse
class HttpRequestMock():
    def __init__(self):
        pass 
def test_handle():
    http_request_mock = HttpRequestMock()
    usecase_spy = ${EntityCap}ListUsecaseSpy()
    controller = ${EntityCap}ListController(
        usecase=usecase_spy
    )
    response = controller.handle(
        http_request=http_request_mock
    )
    print()
    print(response.status_code)
    assert isinstance(response,HTTPResponse)
EOF

  echo "✓ Recriados tests: $entity (insert/update/delete/list)"
  echo ""
done

echo "Concluído."