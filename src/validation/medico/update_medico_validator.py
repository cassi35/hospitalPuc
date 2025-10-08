

from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_medico_validator(body:dict) -> None:
    body_validator = Validator({
       "nome":{"type":"string","required":True,"empty":False},
       "cpf":{"type":"string","required":True,"empty":False},
       "especialidade_id":{"type":"integer","required":True,"empty":False},
        "telefone":{"type":"string","required":True,"empty":False},
        "email":{"type":"string","required":True,"empty":False},
        "status":{"type":"string","required":True,"empty":False,"allowed":["ativo","nao ativo"]},
          "usuario_id":{"type":"integer","required":True,"empty":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)