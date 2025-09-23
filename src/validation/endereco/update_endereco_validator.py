from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_endereco_validator(body:dict):
    body_validator = Validator({
        "rua": {"type": "string", "required": False, "empty": False},
        "bairro": {"type": "string", "required": False, "empty": False},
        "cidade": {"type": "string", "required": False, "empty": False},
        "estado": {"type": "string", "required": False, "empty": False},
        "cep": {"type": "string", "required": False, "empty": False, "minlength": 8, "maxlength": 8},
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)
