from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.paciente.insert_paciente_composer import insert_paciente_composer
from src.main.composers.paciente.update_paciente_composer import update_paciente_composer
from src.main.composers.paciente.list_paciente_composer import list_paciente_composer
from src.main.composers.paciente.delete_paciente_composer import delete_paciente_composer
from src.validation.paciente.insert_paciente_validator import insert_paciente_validator
from src.validation.paciente.update_paciente_validator import update_paciente_validator
from src.validation.paciente.delete_paciente_validator import delete_paciente_validator
from src.errors.error_handler import handle_errors
paciente_router = APIRouter()
@paciente_router.post('/')
async def insert_paciente(request: Request):
    try:
        body = await request.json()
        await insert_paciente_validator(body)
        return await request_adapter(request, insert_paciente_composer())
    except Exception as error:
        return handle_errors(error)
@paciente_router.patch('/{id}')
async def update_paciente(id:int,request: Request):
    try:
        body = await request.json()
        await update_paciente_validator(body)
        return await request_adapter(request, update_paciente_composer())
    except Exception as error:
        return handle_errors(error)
@paciente_router.get('/')
async def list_paciente(request: Request):
    try:
        return await request_adapter(request, list_paciente_composer())
    except Exception as error:
        return handle_errors(error)
@paciente_router.delete('/{id}')
async def delete_paciente(id:int,request: Request):
    try:
        await delete_paciente_validator(id)
        return await request_adapter(request, delete_paciente_composer())
    except Exception as error:
        return handle_errors(error)