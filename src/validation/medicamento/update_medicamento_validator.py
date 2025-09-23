
from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_medicamento_validator(body:dict) -> None:
    body_validator = Validator({
        "nome":{"type":"string","required":True,"empty":False},
        "descricao":{"type":"string","required":True,"empty":False},
        "fabricante":{"type":"string","required":True,"empty":False},
        "validade":{"type":"string","required":True,"empty":False},
        "quantidade_estoque":{"type":"integer","required":True,"empty":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)