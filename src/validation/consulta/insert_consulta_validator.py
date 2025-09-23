
from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_consulta_validator(body:dict) -> None:
    body_validator = Validator({
        "data_hora":{"type":"string","required":True},
        "paciente_id":{"type":"integer","required":True},
        "medico_id":{"type":"integer","required":True},
        "especialidade_id":{"type":"integer","required":True},
        "status":{"type":"string","required":True, "allowed": ["nao ativo", "ativo"]},
        "observacoes":{"type":"string","required":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)