

from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_internacao_validator(body:dict) -> None:
    body_validator = Validator({
        "paciente_id":{"type":"integer","required":True,"empty":False},
        "medico_id":{"type":"integer","required":True,"empty":False},
        "leito_id":{"type":"integer","required":True,"empty":False},
        "data_entrada":{"type":"string","required":True,"empty":False},
        "status":{"type":"string","required":True,"empty":False,"allowed":["em andamento","obito","alta"]}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)