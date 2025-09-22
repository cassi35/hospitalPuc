#!/bin/bash
# filepath: /home/cassiano/github_projetos/hospitalPuc/templates/gerar_mock.sh

# Navega para o diretório correto
cd "$(dirname "$0")/../tests/data/mock" || exit 1

echo "🚀 Gerando mocks automaticamente..."

# Lista todas as entidades (pastas)
for entity_dir in */; do
    # Remove a barra do final para obter o nome da entidade
    entity=$(basename "$entity_dir")
    
    # Pula __pycache__
    if [[ "$entity" == "__pycache__" ]]; then
        continue
    fi
    
    echo "📁 Processando entidade: $entity"
    
    # Capitaliza primeira letra para o nome da classe
    entity_capitalized=$(echo "$entity" | sed 's/.*/\u&/')
    
    # ================== INSERT SPY ==================
    cat > "$entity/insert_${entity}_spy.py" << EOF
from typing import Dict
from src.domain.models.${entity}_model import ${entity_capitalized}

class ${entity_capitalized}InsertUsecaseSpy:
    def __init__(self):
        self.insert_${entity}_attributes = {}
        self.insert_call_count = 0
        self.insert_was_called = False
        
    def insert(self, ${entity}: ${entity_capitalized}) -> Dict:
        self.insert_call_count += 1
        self.insert_was_called = True
        self.insert_${entity}_attributes = ${entity}.__dict__
        
        return {
            "type": "${entity_capitalized}",
            "count": 1,
            "attributes": {
                **self.insert_${entity}_attributes
            }
        }
EOF
    
    # ================== UPDATE SPY ==================
    cat > "$entity/update_${entity}_spy.py" << EOF
from typing import Dict
from src.domain.models.${entity}_model import ${entity_capitalized}

class ${entity_capitalized}UpdateUsecaseSpy:
    def __init__(self):
        self.update_call_count = 0
        self.update_was_called = False
        self.update_${entity}_id = None
        self.update_${entity}_attributes = {}
        
    def update(self, ${entity}_id: int, ${entity}: ${entity_capitalized}) -> Dict:
        self.update_call_count += 1
        self.update_was_called = True
        self.update_${entity}_id = ${entity}_id
        self.update_${entity}_attributes = ${entity}.__dict__
        
        return {
            "type": "${entity_capitalized}",
            "count": 1,
            "attributes": {
                "id": ${entity}_id,
                **self.update_${entity}_attributes
            }
        }
EOF
    
    # ================== DELETE SPY ==================
    cat > "$entity/delete_${entity}_spy.py" << EOF
from typing import Dict

class ${entity_capitalized}DeleteUsecaseSpy:
    def __init__(self):
        self.delete_call_count = 0
        self.delete_was_called = False
        self.delete_${entity}_id = None

    def delete(self, ${entity}_id: int) -> Dict:
        self.delete_call_count += 1
        self.delete_was_called = True
        self.delete_${entity}_id = ${entity}_id

        return {
            "type": "${entity_capitalized}",
            "count": 1,
            "attributes": {
                "id": ${entity}_id
            }
        }
EOF
    
    echo "  ✅ Criado: insert_${entity}_spy.py"
    echo "  ✅ Criado: update_${entity}_spy.py" 
    echo "  ✅ Criado: delete_${entity}_spy.py"
    echo ""
done

echo "🎉 Todos os mocks foram gerados com sucesso!"
echo "📝 Arquivos list_*_spy.py devem ser criados manualmente conforme solicitado."
echo ""
echo "Entidades processadas:"
ls -d */ | grep -v __pycache__ | sed 's|/||'