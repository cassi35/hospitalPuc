#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.."; pwd)"
DOMAIN_USECASES_DIR="$ROOT_DIR/src/domain/usecases"
PRESENTATION_CONTROLLERS_DIR="$ROOT_DIR/src/presentation/controllers"

echo "Recriando controllers (exceto endereco) em: $PRESENTATION_CONTROLLERS_DIR"
echo ""

shopt -s nullglob
for entity_path in "$DOMAIN_USECASES_DIR"/*/; do
  entity="$(basename "$entity_path")"
  [[ "$entity" == "__pycache__" ]] && continue
  [[ "$entity" == "endereco" ]] && { echo "• Pulando endereco (não será alterado)"; echo ""; continue; }

  entity_cap="${entity^}"  # Capitaliza primeira letra
  dest_dir="$PRESENTATION_CONTROLLERS_DIR/$entity"
  mkdir -p "$dest_dir"

  # Apaga controllers existentes da entidade (mantém __init__.py)
  rm -f "$dest_dir"/insert_"$entity"_controller.py \
        "$dest_dir"/update_"$entity"_controller.py \
        "$dest_dir"/delete_"$entity"_controller.py \
        "$dest_dir"/list_"$entity"_controller.py || true

  # INSERT (segue exatamente o padrão do Endereco)
  cat > "$dest_dir/insert_${entity}_controller.py" <<EOF
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.${entity}.insert_${entity} import ${entity_cap}InsertUseCase as ${entity_cap}InsertInterface
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.models.${entity}_model import ${entity_cap} as ${entity_cap}Domain
class ${entity_cap}InsertController(ControllerInterface):
    def __init__(self,usecase:${entity_cap}InsertInterface)-> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        ${entity} = ${entity_cap}Domain(**http_request.body)
        response = self.usecase.insert(
            ${entity}=${entity}
        )
        return HTTPResponse(status_code=200,body=response)
EOF

  # UPDATE (segue exatamente o padrão do Endereco)
  cat > "$dest_dir/update_${entity}_controller.py" <<EOF
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.${entity}.update_${entity} import ${entity_cap}UpdateUseCase as ${entity_cap}UpdateInterface
from src.domain.models.${entity}_model import ${entity_cap} as ${entity_cap}Domain
class ${entity_cap}UpdateController(ControllerInterface):
    def __init__(self,usecase:${entity_cap}UpdateInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest) -> HTTPResponse:
        ${entity}_id = int(http_request.path_params["id"])
        ${entity} = ${entity_cap}Domain(**http_request.body) 
        ${entity}.id = ${entity}_id
        response = self.usecase.update(
            ${entity}_id=${entity}_id,
            ${entity}=${entity}
        )
        return HTTPResponse(status_code=200,body=response)
EOF

  # DELETE (segue exatamente o padrão do Endereco)
  cat > "$dest_dir/delete_${entity}_controller.py" <<EOF
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.usecases.${entity}.delete_${entity} import ${entity_cap}DeleteUseCase as ${entity_cap}DeleteInterface
class ${entity_cap}DeleteController(ControllerInterface): 
    def __init__(self,usecase:${entity_cap}DeleteInterface) -> None:
        self.usecase = usecase
    def handle(self, http_request:HTTPRequest)-> HTTPResponse:
        ${entity}_id = int(http_request.path_params["id"])
        response = self.usecase.delete(
            ${entity}_id=${entity}_id
        )
        return HTTPResponse(status_code=200,body=response)
EOF

  # LIST (segue exatamente o padrão do Endereco)
  cat > "$dest_dir/list_${entity}_controller.py" <<EOF
from src.presentation.http_types.http_request import HTTPRequest
from src.presentation.http_types.http_response import HTTPResponse
from src.domain.usecases.${entity}.list_${entity} import ${entity_cap}ListUseCase as ${entity_cap}ListInterface
from src.presentation.interfaces.controller_interface import ControllerInterface
class ${entity_cap}ListController(ControllerInterface):
    def __init__(self,usecase:${entity_cap}ListInterface) -> None:
        self.usecase = usecase
    def handle(self,http_request:HTTPRequest) -> HTTPResponse:
        response = self.usecase.list()
        return HTTPResponse(status_code=200,body=response)
EOF

  echo "✓ Recriado: $entity (insert/update/delete/list)"
  echo ""
done

echo "Concluído."