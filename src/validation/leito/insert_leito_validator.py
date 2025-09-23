

from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_internacao_validator(body:dict) -> None:
    body_validator = Validator({
        "numero_leito":{"type":"string","required":True,"empty":False},
        "setor_id":{"type":"integer","required":True,"empty":False},
        "tipo":{"type":"string","required":True,"empty":False,"allowed":["UTI Pediátrica","Enfermaria","UTI adulto"]},
        "status":{"type":"string","required":True,"empty":False,"allowed":["disponivel","ocupado"]}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)