from fastapi import APIRouter,Request
from src.main.adapter.request_adapter import request_adapter
from src.main.composers.email.resend_verification_token import resend_verification_token_composer
from src.main.composers.email.send_reset_password import send_reset_password_composer
from src.main.composers.email.send_token import send_verification_token_composer
from src.main.composers.email.send_welcome import send_welcome_email_composer
from src.validation.email.resend_verification_token import send_resend_verification_token_validator
from src.validation.email.send_reset_password import send_reset_password_validator
from src.validation.email.send_token import send_token_validator
from src.validation.email.send_welcome import send_welcome_validator
from src.errors.error_handler import handle_errors
email_router = APIRouter()
@email_router.post('/send-verification-token')
async def send_verification_token(request:Request):
    try:
        body = await request.json()
        send_token_validator(body)
        return await request_adapter(request,send_verification_token_composer())
    except Exception as error:
        return handle_errors(error)
@email_router.post('/resend-verification-token')
async def resend_verification_token(request:Request):
    try:
        body = await request.json()
        send_resend_verification_token_validator(body)
        return await request_adapter(request,resend_verification_token_composer())
    except Exception as error:
        return handle_errors(error)
@email_router.post('/send-reset-password')
async def send_reset_password(request:Request):
    try:
        body = await request.json()
        send_reset_password_validator(body)
        return await request_adapter(request,send_reset_password_composer())
    except Exception as error:
        return handle_errors(error)
@email_router.post('/send-welcome-email')
async def send_welcome_email(request:Request):
    try:
        body = await request.json()
        send_welcome_validator(body)
        return await request_adapter(request,send_welcome_email_composer())
    except Exception as error:
        return handle_errors(error)

