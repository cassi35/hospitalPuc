from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart 
from src.infra.email.templates.resend_verification_token import resend_verification_token_template
from src.infra.email.templates.send_token import send_token_template
from src.infra.email.templates.send_welcome import send_welcome_email_template
from src.infra.email.templates.send_reset_password import send_reset_password_email_template
from src.infra.email.email_config import email_settings
from src.domain.models.user_email import UserEmail
from src.data.interfaces.stmp_service_interface import SMTPServiceInterface 
from src.errors.types.SMTPException import SMTPException
class SMTPEmailService(SMTPServiceInterface):
    def __init__(self):
        self.config = email_settings
        self.server = None
        # self.message = MIMEMultipart('alternative')
    def send_token(self, token:str, email:str) -> bool:
        html = send_token_template(token=token)
        text = f"Código: {token}"
        ok = self._send_email(email, "Código de Verificação", html, text)
        if not ok:
            raise SMTPException("Falha ao enviar token")
        return True
    def send_welcome_email(self, email:UserEmail)-> bool:
        html = send_welcome_email_template(user_email=email)
        text = f"Bem-vindo, {email.name}"
        ok = self._send_email(email.email, "Bem-vindo", html, text)
        if not ok:
            raise SMTPException("Falha ao enviar email de boas-vindas")
        return True
    def send_reset_password_email(self, token:str, email:str) -> bool:
        html = send_reset_password_email_template(token)
        text = f"Código para redefinir: {token}"
        ok = self._send_email(email, "Redefinição de Senha", html, text)
        if not ok:
            raise SMTPException("Falha ao enviar reset de senha")
        return True
    def resend_verification_token(self, token:str, email:str) -> bool:
        html = resend_verification_token_template(token)
        text = f"Novo código: {token}"
        ok = self._send_email(email, "Reenvio de Código", html, text)
        if not ok:
            raise SMTPException("Falha ao reenviar token")
        return True
    # def _send_email(self, to_email: str, subject: str, html_content: str, text_content: str) -> bool:
    #     try:
    #         self.message['from'] = f"{self.config.MAIL_FROM_NAME} <{self.config.MAIL_FROM}>"
    #         self.message['to'] = to_email
    #         self.message['subject'] = subject
    #         self.message.attach(MIMEText(text_content, 'plain', 'utf-8'))
    #         self.message.attach(MIMEText(html_content, 'html', 'utf-8'))
    #         context = ssl.create_default_context()
    #         self.server.starttls(context=context)
    #         self.server.login(
    #             str(self.config.MAIL_USERNAME).strip().strip('"').strip("'"),
    #             str(self.config.MAIL_PASS).strip().strip('"').strip("'")
    #         )
    #         self.server.send_message(self.message)
    #         return True
    #     except Exception as e:
    #         raise SMTPException(f"Erro ao enviar email: {e}")
    def _send_email(self, to_email: str, subject: str, html_content: str, text_content: str) -> bool:
        try:
            # ✅ Conecta só quando necessário
            if self.server is None:
                self.server = SMTP(self.config.MAIL_SERVER, self.config.MAIL_PORT)
                context = ssl.create_default_context()
                self.server.starttls(context=context)
                self.server.login(
                    str(self.config.MAIL_USERNAME).strip().strip('"').strip("'"),
                    str(self.config.MAIL_PASS).strip().strip('"').strip("'")
                )
            
            # ✅ Nova mensagem a cada envio
            message = MIMEMultipart('alternative')
            message['from'] = f"{self.config.MAIL_FROM_NAME} <{self.config.MAIL_FROM}>"
            message['to'] = to_email
            message['subject'] = subject
            message.attach(MIMEText(text_content, 'plain', 'utf-8'))
            message.attach(MIMEText(html_content, 'html', 'utf-8'))
            
            self.server.send_message(message)
            return True
        except Exception as e:
            # ✅ Reset connection em caso de erro
            self.server = None
            raise SMTPException(f"Erro ao enviar email: {e}")