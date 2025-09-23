



from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_prescricao_validator(body:dict) -> None:
    body_validator = Validator({
        "dosagem":{"type":"integer","required":True,"empty":False},
        "paciente_id":{"type":"integer","required":True,"empty":False},
        "medico_id":{"type":"integer","required":True,"empty":False},
        "medicamento_id":{"type":"integer","required":True,"empty":False},
        "frequencia":{"type":"integer","required":True,"empty":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)