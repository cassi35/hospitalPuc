from fastapi import APIRouter,Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.consulta.insert_consulta_composer import insert_consulta_composer
from src.main.composers.consulta.delete_consulta_composer import delete_consulta_composer
from src.main.composers.consulta.list_consulta_composer import list_consulta_composer
from src.main.composers.consulta.update_consulta_composer import update_consulta_composer
from src.validation.consulta.delete_consulta_validator import delete_consulta_validator
from src.validation.consulta.insert_consulta_validator import insert_consulta_validator
from src.validation.consulta.update_consulta_validator import update_consulta_validator
from src.errors.error_handler import handle_errors
consulta_router = APIRouter()
@consulta_router.post('/')
async def insert_consulta(request:Request):
    try:
        body = await request.json()
        await insert_consulta_validator(body)
        return await request_adapter(request,insert_consulta_composer())
    except Exception as error:
        return handle_errors(error)
@consulta_router.patch('/{id}')
async def update_consulta(id:int, request:Request):
    try:
        body = await request.json()
        await update_consulta_validator(body)
        return await request_adapter(request,update_consulta_composer())
    except Exception as error:
        return handle_errors(error)
@consulta_router.delete('/{id}')
async def delete_consulta(id:int,request:Request):
    try:
        await delete_consulta_validator(id)
        return await request_adapter(request,delete_consulta_composer())
    except Exception as error:
        return handle_errors(error)
@consulta_router.get('/')
async def list_consulta(request:Request):
    try:
        return await request_adapter(request,list_consulta_composer())
    except Exception as error:
        return handle_errors(error) 
    