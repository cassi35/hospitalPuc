#!/bin/bash

USECASE_DIR="../src/data/usecases"

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
from typing import Dict
from src.domain.usecases.${pasta}.insert_${pasta} import ${entidade}InsertUseCase as ${entidade}InsertInterface
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface 
from src.infra.db.entities.${pasta} import ${entidade}

class ${entidade}InsertUseCase(${entidade}InsertInterface):
    def __init__(self, ${pasta}_repository: ${entidade}RepositoryInterface):
        self.${pasta}_repository = ${pasta}_repository
    
    def insert(self, ${pasta}: ${entidade}) -> Dict:
        pass
EOF

  # update
  cat > "$pasta_destino/update_${pasta}.py" <<EOF
from typing import Dict
from src.domain.usecases.${pasta}.update_${pasta} import ${entidade}UpdateUseCase as ${entidade}UpdateInterface
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface 
from src.infra.db.entities.${pasta} import ${entidade}

class ${entidade}UpdateUseCase(${entidade}UpdateInterface):
    def __init__(self, ${pasta}_repository: ${entidade}RepositoryInterface):
        self.${pasta}_repository = ${pasta}_repository
    
    def update(self, ${pasta}_id: int, ${pasta}: ${entidade}) -> Dict:
        pass
EOF

  # delete
  cat > "$pasta_destino/delete_${pasta}.py" <<EOF
from src.domain.usecases.${pasta}.delete_${pasta} import ${entidade}DeleteUseCase as ${entidade}DeleteInterface
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}DeleteUseCase(${entidade}DeleteInterface):
    def __init__(self, ${pasta}_repository: ${entidade}RepositoryInterface):
        self.${pasta}_repository = ${pasta}_repository
    
    def delete(self, ${pasta}_id: int) -> None:
        pass
EOF

  # list
  cat > "$pasta_destino/list_${pasta}.py" <<EOF
from typing import List, Dict
from src.domain.usecases.${pasta}.list_${pasta} import ${entidade}ListUseCase as ${entidade}ListInterface
from src.data.interfaces.${pasta}_interface_repository import ${entidade}RepositoryInterface

class ${entidade}ListUseCase(${entidade}ListInterface):
    def __init__(self, ${pasta}_repository: ${entidade}RepositoryInterface):
        self.${pasta}_repository = ${pasta}_repository
    
    def list(self) -> List[Dict]:
        pass
EOF

  # __init__.py
  > "$pasta_destino/__init__.py"

  echo "Templates de implementação gerados para $pasta"
done