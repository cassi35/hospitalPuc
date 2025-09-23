
from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_setor_validator(body:dict) -> None:
    body_validator = Validator({
        "nome":{"type":"string","required":True,"empty":False},
        "andar":{"type":"integer","required":True,"empty":False},
        "capacidade":{"type":"integer","required":True,"empty":False},
        "responsavel":{"type":"integer","required":True,"empty":False},
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)