from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def send_welcome_validator(email:dict)-> None:
    body_validator = Validator({
        "email": {
            "type": "string",
            "required": True,
            "empty": False,
            "regex": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        },
        "name":{"type":"string","required":True,"empty":False}
    })
    if not body_validator.validate(email):
        raise HttpUnprocessableEntityError(body_validator.errors)