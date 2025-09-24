from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.funcionario.insert_funcionario_composer import insert_funcionario_composer
from src.main.composers.funcionario.delete_funcionario_composer import delete_funcionario_composer
from src.main.composers.funcionario.list_funcionario_composer import list_funcionario_composer
from src.main.composers.funcionario.update_funcionario_composer import update_funcionario_composer
from src.validation.funcionario.delete_funcionario_validator import delete_funcionario_validator
from src.validation.funcionario.insert_funcionario_validator import insert_funcionario_validator
from src.validation.funcionario.update_funcionario_validator import update_funcionario_validator
from src.errors.error_handler import handle_errors

funcionario_router = APIRouter()

@funcionario_router.post('/')
async def insert_funcionario(request: Request):
    try:
        body = await request.json()
        await insert_funcionario_validator(body)
        return await request_adapter(request, insert_funcionario_composer())
    except Exception as error:
        return handle_errors(error)
@funcionario_router.patch('/{id}')
async def update_funcionario(id:int,request: Request):
    try:
        body = await request.json()
        await update_funcionario_validator(body)
        return await request_adapter(request, update_funcionario_composer())
    except Exception as error:
        return handle_errors(error)
@funcionario_router.get('/')
async def list_funcionario(request: Request):
    try:
        return await request_adapter(request, list_funcionario_composer())
    except Exception as error:
        return handle_errors(error)
@funcionario_router.delete('/{id}')
async def delete_funcionario(id:int,request: Request):
    try:
        await delete_funcionario_validator(id)
        return await request_adapter(request, delete_funcionario_composer())
    except Exception as error:
        return handle_errors(error)