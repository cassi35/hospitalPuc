


from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_convenio_validator(body:dict) -> None:
    body_validator = Validator({
    "nome":{"type":"string","required":True,"empty":False},
    "tipo_plano":{"type":"string","required":True,"empty":False,"allowed":["Familiar","Individual","Empresarial"]},
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)