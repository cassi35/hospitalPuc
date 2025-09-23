from fastapi import APIRouter,Request
from fastapi import Depends,status
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.endereco.insert_endereco_composer import insert_endereco_composer
from src.main.composers.endereco.update_endereco_composer import update_endereco_composer
from src.main.composers.endereco.delete_endereco_composer import delete_endereco_composer
from src.main.composers.endereco.list_endereco_composer import list_endereco_composer
from src.validation.endereco.insert_endereco_validator import insert_endereco_validator
from src.errors.error_handler import handle_errors
from src.validation.endereco.update_endereco_validator import update_endereco_validator
from src.validation.endereco.delete_endereco_validator import delete_endereco_validator

endereco_router = APIRouter()
@endereco_router.post('/')
async def insert_endereco(request:Request):
    try:
        body = await request.json()
        await insert_endereco_validator(body)
        return await request_adapter(request,insert_endereco_composer())

    except Exception as error:
        return handle_errors(error)
@endereco_router.patch('/{id}')
async def update_endereco(id: int, request: Request):
    try:
        body = await request.json()
        await update_endereco_validator(body)
        return await request_adapter(request, update_endereco_composer())
    except Exception as error:
        return handle_errors(error)
@endereco_router.delete('/{id}')
async def delete_endereco(id:int , request:Request):
    try:  
        await delete_endereco_validator(id) 
        return await request_adapter(request,delete_endereco_composer())
    except Exception as error:
        return handle_errors(error)
@endereco_router.get('/')
async def list_endereco(request:Request):
    try:
        return await request_adapter(request,list_endereco_composer())
    except Exception as error:
        return handle_errors(error) 
