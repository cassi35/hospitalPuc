from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def send_reset_password_validator(body:dict)-> None:
    body_validator = Validator(
        {
            "email":{"type":"string","required":True,"empty":False,"regex":r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"},
            "token":{"type":"integer","required":True,"empty":False}
        }
    )
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)