from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.setor.insert_setor_composer import insert_setor_composer
from src.main.composers.setor.update_setor_composer import update_setor_composer
from src.main.composers.setor.list_setor_composer import list_setor_composer
from src.main.composers.setor.delete_setor_composer import delete_setor_composer
from src.validation.setor.insert_setor_validator import insert_setor_validator 
from src.validation.setor.update_setor_validator import update_setor_validator
from src.validation.setor.delete_setor_validator import delete_setor_validator
from src.errors.error_handler import handle_errors
setor_router = APIRouter()
@setor_router.post('/')
async def insert_setor(request: Request):
    try:
        body = await request.json()
        await insert_setor_validator(body)
        return await request_adapter(request, insert_setor_composer())
    except Exception as error:
        return handle_errors(error)
@setor_router.patch('/{id}')
async def update_setor(id:int,request: Request):
    try:
        body = await request.json()
        await update_setor_validator(body)
        return await request_adapter(request, update_setor_composer())
    except Exception as error:
        return handle_errors(error)
@setor_router.get('/')
async def list_setor(request: Request):
    try:
        return await request_adapter(request, list_setor_composer())
    except Exception as error:
        return handle_errors(error)
@setor_router.delete('/{id}')
async def delete_setor(id:int,request: Request):
    try:
        await delete_setor_validator(id)
        return await request_adapter(request, delete_setor_composer())
    except Exception as error:
        return handle_errors(error)
    