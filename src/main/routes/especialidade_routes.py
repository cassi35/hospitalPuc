from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.especialidade.insert_especialidade_composer import insert_especialidade_composer
from src.main.composers.especialidade.update_especialidade_composer import update_especialidade_composer
from src.main.composers.especialidade.delete_especialidade_composer import delete_especialidade_composer
from src.main.composers.especialidade.list_especialidade_composer import list_especialidade_composer
from src.validation.especialidade.delete_especialidade_validator import delete_especialidade_validator
from src.validation.especialidade.insert_especialidade_validator import insert_especialidade_validator
from src.validation.especialidade.update_especialidade_validator import update_especialidade_validator
from src.errors.error_handler import handle_errors
especialidade_router = APIRouter()
@especialidade_router.post('/')
async def insert_especialidade(request:Request):
    try:
        body = await request.json()
        await insert_especialidade_validator(body)
        return await request_adapter(request,insert_especialidade_composer())
    except Exception as error:
        return handle_errors(error)
@especialidade_router.patch('/{id}')
async def update_especialidade(id: int, request: Request):
    try:
        body = await request.json()
        await update_especialidade_validator(body)
        return await request_adapter(request,update_especialidade_composer())
    except Exception as error:
        return handle_errors(error)
@especialidade_router.delete('/{id}')
async def delete_especialidade(id:int , request:Request):
    try:  
        await delete_especialidade_validator(id) 
        return await request_adapter(request,delete_especialidade_composer())
    except Exception as error:
        return handle_errors(error)
@especialidade_router.get('/')
async def list_especialidade(request:Request):
    try:
        return await request_adapter(request,list_especialidade_composer())
    except Exception as error:
        return handle_errors(error)