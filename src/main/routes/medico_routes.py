from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.medico.insert_medico_composer import insert_medico_composer
from src.main.composers.medico.delete_medico_composer import delete_medico_composer
from src.main.composers.medico.list_medico_composer import list_medico_composer
from src.main.composers.medico.update_medico_composer import update_medico_composer
from src.validation.medico.delete_medico_validator import delete_medico_validator
from src.validation.medico.insert_medico_validator import insert_medico_validator
from src.validation.medico.update_medico_validator import update_medico_validator
from src.errors.error_handler import handle_errors

medico_router = APIRouter()

@medico_router.post('/')
async def insert_medico(request: Request):
    try:
        body = await request.json()
        await insert_medico_validator(body)
        return await request_adapter(request, insert_medico_composer())
    except Exception as error:
        return handle_errors(error)

@medico_router.patch('/{id}')
async def update_medico(id:int,request: Request):
    try:
        body = await request.json()
        await update_medico_validator(body)
        return await request_adapter(request, update_medico_composer())
    except Exception as error:
        return handle_errors(error)

@medico_router.get('/')
async def list_medico(request: Request):
    try:
        return await request_adapter(request, list_medico_composer())
    except Exception as error:
        return handle_errors(error)

@medico_router.delete('/{id}')
async def delete_medico(id:int,request: Request):
    try:
        await delete_medico_validator(id)
        return await request_adapter(request, delete_medico_composer())
    except Exception as error:
        return handle_errors(error)