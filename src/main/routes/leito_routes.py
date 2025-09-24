from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.leito.insert_leito_composer import insert_leito_composer
from src.main.composers.leito.delete_leito_composer import delete_leito_composer
from src.main.composers.leito.list_leito_composer import list_leito_composer
from src.main.composers.leito.update_leito_composer import update_leito_composer
from src.validation.leito.delete_leito_validator import delete_leito_validator
from src.validation.leito.insert_leito_validator import insert_leito_validator
from src.validation.leito.update_leito_validator import update_leito_validator
from src.errors.error_handler import handle_errors

leito_router = APIRouter()

@leito_router.post('/')
async def insert_leito(request: Request):
    try:
        body = await request.json()
        await insert_leito_validator(body)
        return await request_adapter(request, insert_leito_composer())
    except Exception as error:
        return handle_errors(error)

@leito_router.patch('/{id}')
async def update_leito(id:int,request: Request):
    try:
        body = await request.json()
        await update_leito_validator(body)
        return await request_adapter(request, update_leito_composer())
    except Exception as error:
        return handle_errors(error)

@leito_router.get('/')
async def list_leito(request: Request):
    try:
        return await request_adapter(request, list_leito_composer())
    except Exception as error:
        return handle_errors(error)

@leito_router.delete('/{id}')
async def delete_leito(id:int,request: Request):
    try:
        await delete_leito_validator(id)
        return await request_adapter(request, delete_leito_composer())
    except Exception as error:
        return handle_errors(error)