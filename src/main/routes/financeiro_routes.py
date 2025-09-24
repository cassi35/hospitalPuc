from fastapi import APIRouter,Request
from src.main.adapter.request_adapter import request_adapter

from src.main.composers.financeiro.delete_financeiro_composer import delete_financeiro_composer
from src.main.composers.financeiro.insert_financeiro_composer import insert_financeiro_composer
from src.main.composers.financeiro.list_financeiro_composer import list_financeiro_composer
from src.main.composers.financeiro.update_financeiro_composer import update_financeiro_composer
from src.validation.financeiro.delete_financeiro_validator import delete_financeiro_validator
from src.validation.financeiro.insert_financeiro_validator import insert_financeiro_validator
from src.validation.financeiro.update_financeiro_validator import update_financeiro_validator
from src.errors.error_handler import handle_errors
financeiro_routes = APIRouter()
@financeiro_routes.post('/')
async def insert_financeiro(request:Request):
    try:
        body = await request.json()
        await insert_financeiro_validator(body)
        return await request_adapter(request,insert_financeiro_composer())
    except Exception as error:
        return handle_errors(error)
@financeiro_routes.patch('/{id}')
async def update_financeiro(id:int, request:Request):
    try:
        body = await request.json()
        await update_financeiro_validator(body)
        return await request_adapter(request,update_financeiro_composer())
    except Exception as error:
        return handle_errors(error)
@financeiro_routes.get('/')
async def list_financeiro(request:Request):
    try: 
        return await request_adapter(request,list_financeiro_composer())
    except Exception as error:
        return handle_errors(error)
@financeiro_routes.delete('/{id}')
async def delete_financeiro(id:int, request:Request):
    try:
        await delete_financeiro_validator(id)
        return await request_adapter(request,delete_financeiro_composer())
    except Exception as error:
        return handle_errors(error)