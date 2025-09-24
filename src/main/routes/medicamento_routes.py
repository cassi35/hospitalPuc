from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.medicamento.insert_medicamento_composer import insert_medicamento_composer
from src.main.composers.medicamento.delete_medicamento_composer import delete_medicamento_composer
from src.main.composers.medicamento.list_medicamento_composer import list_medicamento_composer
from src.main.composers.medicamento.update_medicamento_composer import update_medicamento_composer
from src.validation.medicamento.delete_medicamento_validator import delete_medicamento_validator
from src.validation.medicamento.insert_medicamento_validator import insert_medicamento_validator
from src.validation.medicamento.update_medicamento_validator import update_medicamento_validator
from src.errors.error_handler import handle_errors

medicamento_router = APIRouter()

@medicamento_router.post('/')
async def insert_medicamento(request: Request):
    try:
        body = await request.json()
        await insert_medicamento_validator(body)
        return await request_adapter(request, insert_medicamento_composer())
    except Exception as error:
        return handle_errors(error)

@medicamento_router.patch('/{id}')
async def update_medicamento(id:int,request: Request):
    try:
        body = await request.json()
        await update_medicamento_validator(body)
        return await request_adapter(request, update_medicamento_composer())
    except Exception as error:
        return handle_errors(error)

@medicamento_router.get('/')
async def list_medicamento(request: Request):
    try:
        return await request_adapter(request, list_medicamento_composer())
    except Exception as error:
        return handle_errors(error)

@medicamento_router.delete('/{id}')
async def delete_medicamento(id:int,request: Request):
    try:
        await delete_medicamento_validator(id)
        return await request_adapter(request, delete_medicamento_composer())
    except Exception as error:
        return handle_errors(error)