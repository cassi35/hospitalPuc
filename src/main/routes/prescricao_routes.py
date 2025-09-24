from fastapi import APIRouter, Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.prescricao.insert_prescricao_composer import insert_prescricao_composer
from src.main.composers.prescricao.update_prescricao_composer import update_prescricao_composer
from src.main.composers.prescricao.list_prescricao_composer import list_prescricao_composer
from src.main.composers.prescricao.delete_prescricao_composer import delete_prescricao_composer
from src.validation.prescricao.insert_prescricao_validator import insert_prescricao_validator
from src.validation.prescricao.update_prescricao_validator import update_prescricao_validator
from src.validation.prescricao.delete_prescricao_validator import delete_prescricao_validator
from src.errors.error_handler import handle_errors
prescricao_router = APIRouter()
@prescricao_router.post('/')
async def insert_prescricao(request: Request):
    try:
        body = await request.json()
        await insert_prescricao_validator(body)
        return await request_adapter(request, insert_prescricao_composer())
    except Exception as error:
        return handle_errors(error)
@prescricao_router.patch('/{id}')
async def update_prescricao(id:int,request: Request):
    try:
        body = await request.json()
        await update_prescricao_validator(body)
        return await request_adapter(request, update_prescricao_composer())
    except Exception as error:
        return handle_errors(error)
@prescricao_router.get('/')
async def list_prescricao(request: Request):
    try:
        return await request_adapter(request, list_prescricao_composer())
    except Exception as error:
        return handle_errors(error)
@prescricao_router.delete('/{id}')
async def delete_prescricao(id:int,request: Request):
    try:
        await delete_prescricao_validator(id)
        return await request_adapter(request, delete_prescricao_composer())
    except Exception as error:
        return handle_errors(error)