from fastapi import APIRouter,Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.exame.insert_exame_composer import insert_exame_composer
from src.main.composers.exame.delete_exame_composer import delete_exame_composer
from src.main.composers.exame.list_exame_composer import list_exame_composer
from src.main.composers.exame.update_exame_composer import update_exame_composer
from src.validation.exame.delete_exame_validator import delete_exame_validator 
from src.validation.exame.insert_exame_validator import insert_exame_validator
from src.validation.exame.update_exame_validator import update_exame_validator
from src.errors.error_handler import handle_errors
exame_router = APIRouter()
@exame_router.post('/')
async def insert_exame(request:Request):
    try:
        body = await request.json()
        await insert_exame_validator(body)
        return await request_adapter(request,insert_exame_composer())
    except Exception as error:
        return handle_errors(error)
@exame_router.patch('/{id}')
async def update_exame(id:int, request:Request):
    try:
        body = await request.json()
        await update_exame_validator(body)
        return await request_adapter(request,update_exame_composer())
    except Exception as error:
        return handle_errors(error)
@exame_router.delete('/{id}')
async def delete_exame(id:int,request:Request):
    try:
        await delete_exame_validator(id)
        return await request_adapter(request,delete_exame_composer())
    except Exception as error:
        return handle_errors(error)
@exame_router.get('/')
async def list_exame(request:Request):
    try:
        return await request_adapter(request,list_exame_composer())
    except Exception as error:
        return handle_errors(error)