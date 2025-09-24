from fastapi import APIRouter,Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.convenio.insert_convenio_composer import insert_convenio_composer
from src.main.composers.convenio.update_convenio_composer import update_convenio_composer
from src.main.composers.convenio.delete_convenio_composer import delete_convenio_composer
from src.main.composers.convenio.list_convenio_composer import list_convenio_composer
from src.validation.convenio.delete_convenio_validator import delete_convenio_validator
from src.validation.convenio.insert_convenio_validator import insert_convenio_validator
from src.validation.convenio.update_convenio_validator import update_convenio_validator
from src.errors.error_handler import handle_errors
convenio_router = APIRouter()
@convenio_router.post('/')
async def insert_convenio(request:Request):
    try:
        body = await request.json()
        await insert_convenio_validator(body)
        return await request_adapter(request,insert_convenio_composer())
    except Exception as error:
        return handle_errors(error)
@convenio_router.patch('/{id}')
async def update_convenio(id: int, request: Request):
    try:
        body = await request.json()
        await update_convenio_validator(body)
        return await request_adapter(request,update_convenio_composer())
    except Exception as error:
        return handle_errors(error)
@convenio_router.delete('/{id}')
async def delete_convenio(id:int , request:Request):
    try:  
        await delete_convenio_validator(id) 
        return await request_adapter(request,delete_convenio_composer())
    except Exception as error:
        return handle_errors(error)
@convenio_router.get('/')
async def list_convenio(request:Request):
    try:
        return await request_adapter(request,list_convenio_composer())
    except Exception as error:
        return handle_errors(error)