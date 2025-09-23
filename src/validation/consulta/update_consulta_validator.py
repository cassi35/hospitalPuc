

from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_consulta_validator(body:dict) -> None:
    body_validator = Validator({
        "data_hora":{"type":"datetime","required":True},
        "id_paciente":{"type":"integer","required":True},
        "id_medico":{"type":"integer","required":True},
        "especialidade_id":{"type":"integer","required":True},
        "status":{"type":"string","required":True, "allowed": ["nao ativo", "ativo"]}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)