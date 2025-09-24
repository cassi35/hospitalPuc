from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.internacao.insert_internacao_composer import insert_internacao_composer
from src.main.composers.internacao.delete_internacao_composer import delete_internacao_composer
from src.main.composers.internacao.list_internacao_composer import list_internacao_composer
from src.main.composers.internacao.update_internacao_composer import update_internacao_composer
from src.validation.internacao.delete_internacao_validator import delete_internacao_validator
from src.validation.internacao.insert_internacao_validator import insert_internacao_validator
from src.validation.internacao.update_internacao_validator import update_internacao_validator
from src.errors.error_handler import handle_errors

internacao_router = APIRouter()

@internacao_router.post('/')
async def insert_internacao(request: Request):
    try:
        body = await request.json()
        await insert_internacao_validator(body)
        return await request_adapter(request, insert_internacao_composer())
    except Exception as error:
        return handle_errors(error)

@internacao_router.patch('/{id}')
async def update_internacao(id: int, request: Request):
    try:
        body = await request.json()
        await update_internacao_validator(body)
        return await request_adapter(request, update_internacao_composer())
    except Exception as error:
        return handle_errors(error)

@internacao_router.get('/')
async def list_internacao(request: Request):
    try:
        return await request_adapter(request, list_internacao_composer())
    except Exception as error:
        return handle_errors(error)

@internacao_router.delete('/{id}')
async def delete_internacao(id: int, request: Request):
    try:
        await delete_internacao_validator(id)
        return await request_adapter(request, delete_internacao_composer())
    except Exception as error:
        return handle_errors(error)