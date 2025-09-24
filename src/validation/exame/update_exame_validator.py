




from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_exame_validator(body:dict) -> None:
    body_validator = Validator({
       "tipo_exame":{"type":"string","required":True,"empty":False},
       "data_exame":{"type":"string","required":True,"empty":False},
       "paciente_id":{"type":"integer","required":True,"empty":False,"min":1},
       "medico_id":{"type":"integer","required":True,"empty":False,"min":1},
       "resultado":{"type":"string","required":True,"empty":False},
       "status":{"type":"string","required":True,"empty":False,"allowed":["solicitado","em andamento","concluído"]}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)