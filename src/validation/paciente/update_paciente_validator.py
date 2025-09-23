



from cerberus import Validator
from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def update_paciente_validator(body:dict) -> None:
    body_validator = Validator({
       "nome":{"type":"string","required":True,"empty":False},
       "cpf":{"type":"string","required":True,"empty":False},
       "data_nascimento":{"type":"string","required":True,"empty":False},
       "sexo":{"type":"string","required":True,"empty":False,"allowed":["m","f"]},
        "telefone":{"type":"string","required":True,"empty":False},
        "contato_emergencia":{"type":"string","required":True,"empty":False},
        "alergia":{"type":"string","required":True,"empty":False},
        "convenio_id":{"type":"integer","required":True,"empty":False},
        "endereco_id":{"type":"integer","required":True,"empty":False}
    })
    if not body_validator.validate(body):
        raise HttpUnprocessableEntityError(body_validator.errors)