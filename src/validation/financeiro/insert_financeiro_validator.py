




from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def insert_financeiro_validator(body:dict) -> None:
    body_validator = Validator({
       "paciente_id":{"type":"integer","required":True,"empty":False,"min":1},
       "convenio_id":{"type":"integer","required":True,"empty":False,"min":1},
       "valor":{"type":"float","required":True,"empty":False},
       "data_emissao":{"type":"string","required":True,"empty":False},
       "data_vencimento":{"type":"string","required":True,"empty":False},
       "status":{"type":"string","required":True,"empty":False,"allowed":["pendente","pago","cancelado"]}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)