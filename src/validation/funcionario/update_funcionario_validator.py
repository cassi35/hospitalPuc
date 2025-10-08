
from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_funcionario_validator(body:dict) -> None:
    body_validator = Validator({
        "nome":{"type":"string","required":True,"empty":False},
        "cpf":{"type":"string","required":True,"empty":False,"minlength":11,"maxlength":11},
        "cargo":{"type":"string","required":True,"empty":False,"allowed":["enfermeiro","recepcionista","técnico"]},
        "setor_id":{"type":"integer","required":True,"empty":False},
        "telefone":{"type":"string","required":True,"empty":False},
        "email":{"type":"string","required":True,"empty":False},
        "data_contratacao":{"type":"string","required":True,"empty":False},
          "usuario_id":{"type":"integer","required":True,"empty":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)