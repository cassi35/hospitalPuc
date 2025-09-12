#!/bin/bash

USECASE_DIR="../src/domain/usecases"

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
  pasta_destino="$USECASE_DIR/$pasta"
  mkdir -p "$pasta_destino"

  # insert
  cat > "$pasta_destino/insert_${pasta}.py" <<EOF
from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.${pasta} import ${entidade}

class ${entidade}InsertUseCase(ABC):
    @abstractmethod
    def insert(self, ${pasta}: ${entidade}) -> Dict:
        """Insert new ${pasta} usecase"""
        pass
EOF

  # update
  cat > "$pasta_destino/update_${pasta}.py" <<EOF
from abc import ABC, abstractmethod
from typing import Dict
from src.infra.db.entities.${pasta} import ${entidade}

class ${entidade}UpdateUseCase(ABC):
    @abstractmethod
    def update(self, ${pasta}_id: int, ${pasta}: ${entidade}) -> Dict:
        """Update existing ${pasta} usecase"""
        pass
EOF

  # delete
  cat > "$pasta_destino/delete_${pasta}.py" <<EOF
from abc import ABC, abstractmethod

class ${entidade}DeleteUseCase(ABC):
    @abstractmethod
    def delete(self, ${pasta}_id: int) -> None:
        """Delete ${pasta} by id usecase"""
        pass
EOF

  # list
  cat > "$pasta_destino/list_${pasta}.py" <<EOF
from abc import ABC, abstractmethod
from typing import List, Dict

class ${entidade}ListUseCase(ABC):
    @abstractmethod
    def list(self) -> List[Dict]:
        """List all ${pasta}s usecase"""
        pass
EOF

  # __init__.py (zera o arquivo)
  > "$pasta_destino/__init__.py"

  echo "Templates gerados para $pasta em $pasta_destino"
done