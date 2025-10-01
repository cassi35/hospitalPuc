from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.funcionario_interface_repository import FuncionarioRepositoryInterface
from src.domain.models.funcionario_model import Funcionario as FuncionarioDomain
from src.infra.db.entities.funcionario import Funcionario as FuncionarioEntity

class FuncionarioRepository(FuncionarioRepositoryInterface):
    
    def create(self, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        with BDConnectionHandler() as database:
            try:
                funcionario = FuncionarioEntity(
                    nome=nome,
                    cpf=cpf,
                    cargo=cargo,
                    setor_id=setor_id,
                    telefone=telefone,
                    email=email,
                    data_contratacao=data_contratacao
                )
                database.session.add(funcionario)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, nome: str, cpf: str, cargo: str, setor_id: int, telefone: str, email: str, data_contratacao: str) -> None:
        with BDConnectionHandler() as database:
            try:
                funcionario = database.session.query(FuncionarioEntity).filter_by(id=id).first()
                if funcionario:
                    funcionario.nome = nome
                    funcionario.cpf = cpf
                    funcionario.cargo = cargo
                    funcionario.setor_id = setor_id
                    funcionario.telefone = telefone
                    funcionario.email = email
                    funcionario.data_contratacao = data_contratacao
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                funcionario = database.session.query(FuncionarioEntity).filter_by(id=id).first()
                if funcionario:
                    database.session.delete(funcionario)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> FuncionarioDomain:
        with BDConnectionHandler() as database:
            try:
                funcionario = database.session.query(FuncionarioEntity).filter_by(id=id).first()
                if funcionario:
                    return FuncionarioDomain(
                        id=funcionario.id,
                        nome=funcionario.nome,
                        cpf=funcionario.cpf,
                        cargo=funcionario.cargo,
                        setor_id=funcionario.setor_id,
                        telefone=funcionario.telefone,
                        email=funcionario.email,
                        data_contratacao=funcionario.data_contratacao
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[FuncionarioDomain]:
        with BDConnectionHandler() as database:
            try:
                funcionarios = database.session.query(FuncionarioEntity).all()
                return [
                    FuncionarioDomain(
                        id=funcionario.id,
                        nome=funcionario.nome,
                        cpf=funcionario.cpf,
                        cargo=funcionario.cargo,
                        setor_id=funcionario.setor_id,
                        telefone=funcionario.telefone,
                        email=funcionario.email,
                        data_contratacao=funcionario.data_contratacao
                    ) for funcionario in funcionarios
                ]
            except Exception as e:
                database.session.rollback()
                raise e
        def findByEmail(self, email:str)-> str:
            try:
                with BDConnectionHandler() as database:
                    funcionario = database.session.query(FuncionarioEntity).filter_by(email=email).first()
                    if funcionario:
                        return funcionario.email
                    return None
            except Exception as e:
                raise e