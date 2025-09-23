


from src.errors.types.http_unprocessable_entity import HttpUnprocessableEntityError
async def delete_leito_validator(id:int)-> None:
    if not isinstance(id, int) or id <= 0:
        raise HttpUnprocessableEntityError("ID must be a positive integer.")