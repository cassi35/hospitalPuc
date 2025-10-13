from src.domain.models.auth_model import AuthModel as AuthUserDomain
from src.infra.db.entities.authUser import AuthUser as AuthUserEntity
from src.data.interfaces.auth_interface import AuthRepositoryInterface
from typing import Dict,Optional
from datetime import datetime
from src.infra.db.settings.connection import BDConnectionHandler
class AuthRepository(AuthRepositoryInterface):
    def create_user(self,user_data:dict)-> None:
        with BDConnectionHandler() as database:
            try:
                user_auth = AuthUserEntity(
                    email=user_data['email'],
                    nome=user_data['nome'],
                    senha=user_data['senha'],
                    role=user_data['role'],
                    createdAt=datetime.now(),
                    updatedAt=datetime.now(),
                    is_verified=True
                )
                database.session.add(user_auth)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    def get_user_by_email(self,email:str)-> AuthUserDomain:
        with BDConnectionHandler() as database:
           try:
                user = database.session.query(AuthUserEntity).filter_by(email=email).first()
                if user:
                    return AuthUserDomain(
                        id=user.id,
                        email=user.email,
                        createAt=user.createdAt,
                        is_verified=user.is_verified,
                        role=user.role,
                        senha=user.senha,
                        updateAt=user.updatedAt,
                        nome=user.nome
                        
                    )
                return None
           except Exception as e:
                raise e
    def get_user_by_id(self,user_id:int)-> AuthUserDomain:
        with BDConnectionHandler() as database:
            try:
                user = database.session.query(AuthUserEntity).filter_by(id=user_id).first()
                if user:
                    return AuthUserDomain(
                        id=user.id,
                        email=user.email,
                        createAt=user.createdAt,
                        is_verified=user.is_verified,
                        role=user.role,
                        senha=user.senha,
                        updateAt=user.updatedAt,
                        nome=user.nome
                    )
                return None
            except Exception as e:
                raise e
    def update_user(self,user_id:int,update_data:Dict)-> None:
        with BDConnectionHandler() as database:
            try:
                user = database.session.query(AuthUserEntity).filter_by(id=user_id).first()
                if user:
                    user.email = update_data['email']
                    user.nome = update_data['nome']
                    user.senha = update_data['senha']
                    user.role = update_data['role']
                    user.updatedAt = datetime.now()
                    user.is_verified = update_data['is_verified']
                    database.session.commit()
                return None
            except Exception as e:
                database.session.rollback()
                raise e
