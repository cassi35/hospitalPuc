#!/bin/bash

TESTS_DIR="../tests/src/data/tests"

declare -A entidades=(
  [consulta]="Consulta"
  [endereco]="Endereco"
  [exame]="Exame"
  [medico]="Medico"
  [paciente]="Paciente"
  [convenio]="Convenio"
  [especialidade]="Especialidade"
  [financeiro]="Financeiro"
  [funcionario]="Funcionario"
  [internacao]="Internacao"
  [leito]="Leito"
  [medicamento]="Medicamento"
  [prescricao]="Prescricao"
  [setor]="Setor"
)

for pasta in "${!entidades[@]}"; do
  entidade=${entidades[$pasta]}
  pasta_destino="$TESTS_DIR/$pasta"
  mkdir -p "$pasta_destino"

  # insert spy
  cat > "$pasta_destino/${pasta}_insert_spy.py" <<EOF
from typing import Dict
from src.infra.db.entities.${pasta} import ${entidade}
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}InsertSpy(${entidade}RepositoryInterface):
    def __init__(self) -> None:
        self.insert_${pasta}_attributes = {}
        self.insert_${pasta}_call_count = 0

    def insert_${pasta}(self, ${pasta}: ${entidade}) -> None:
        self.insert_${pasta}_attributes = vars(${pasta})
        self.insert_${pasta}_call_count += 1
EOF

  # update spy
  cat > "$pasta_destino/${pasta}_update_spy.py" <<EOF
from typing import Dict
from src.infra.db.entities.${pasta} import ${entidade}
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}UpdateSpy(${entidade}RepositoryInterface):
    def __init__(self) -> None:
        self.update_${pasta}_attributes = {}
        self.update_${pasta}_call_count = 0

    def update_${pasta}(self, ${pasta}_id: int, ${pasta}: ${entidade}) -> None:
        self.update_${pasta}_attributes = vars(${pasta})
        self.update_${pasta}_attributes['id'] = ${pasta}_id
        self.update_${pasta}_call_count += 1
EOF

  # delete spy
  cat > "$pasta_destino/${pasta}_delete_spy.py" <<EOF
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}DeleteSpy(${entidade}RepositoryInterface):
    def __init__(self) -> None:
        self.delete_${pasta}_id = None
        self.delete_${pasta}_call_count = 0

    def delete_${pasta}(self, ${pasta}_id: int) -> None:
        self.delete_${pasta}_id = ${pasta}_id
        self.delete_${pasta}_call_count += 1
EOF

  # list spy
  cat > "$pasta_destino/${pasta}_list_spy.py" <<EOF
from typing import List, Dict
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}ListSpy(${entidade}RepositoryInterface):
    def __init__(self) -> None:
        self.list_${pasta}_call_count = 0
        self.list_${pasta}_return = []

    def list_${pasta}(self) -> List[Dict]:
        self.list_${pasta}_call_count += 1
        return self.list_${pasta}_return
EOF

  # __init__.py
  > "$pasta_destino/__init__.py"

  echo "Spies de teste gerados para $pasta"
done