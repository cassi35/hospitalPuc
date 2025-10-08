from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medico_interface_repository import MedicoRepositoryInterface
from src.domain.models.medico_model import Medico as MedicoDomain
from src.infra.db.entities.medico import Medico as MedicoEntity

class MedicoRepository(MedicoRepositoryInterface):
    
    def create(self, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str,usuario_id:int) -> None:
        with BDConnectionHandler() as database:
            try:
                medico = MedicoEntity(
                    nome=nome,
                    cpf=cpf,
                    especialidade_id=especialidade_id,
                    telefone=telefone,
                    email=email,
                    status=status,
                    usuario_id=usuario_id
                )
                database.session.add(medico)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e 
    
    def update(self, id: int, nome: str, cpf: str, especialidade_id: int, telefone: str, email: str, status: str,usuario_id:int) -> None:
            with BDConnectionHandler() as database:
                try:
                    medico = database.session.query(MedicoEntity).filter_by(id=id).first()
                    if medico:
                        medico.nome = nome
                        medico.cpf = cpf
                        medico.especialidade_id = especialidade_id
                        medico.telefone = telefone
                        medico.email = email
                        medico.status = status
                        medico.usuario_id = usuario_id
                        database.session.commit()
                except Exception as e:
                    database.session.rollback()
                    raise e

    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                medico = database.session.query(MedicoEntity).filter_by(id=id).first()
                if medico:
                    database.session.delete(medico)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> MedicoDomain:
        with BDConnectionHandler() as database:
            try:
                medico = database.session.query(MedicoEntity).filter_by(id=id).first()
                if medico:
                    return MedicoDomain(
                        id=medico.id,
                        nome=medico.nome,
                        cpf=medico.cpf,
                        especialidade_id=medico.especialidade_id,
                        telefone=medico.telefone,
                        email=medico.email,
                        status=medico.status, 
                        usuario_id=medico.usuario_id                   
                        )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[MedicoDomain]:
        with BDConnectionHandler() as database:
            try:
                medicos = database.session.query(MedicoEntity).all()
                return [
                    MedicoDomain(
                        id=medico.id,
                        nome=medico.nome,
                        cpf=medico.cpf,
                        especialidade_id=medico.especialidade_id,
                        telefone=medico.telefone,
                        email=medico.email,
                        status=medico.status,
                        usuario_id=medico.usuario_id
                    ) for medico in medicos
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findByCpf(self, cpf: str) -> MedicoDomain:
        with BDConnectionHandler() as database:
            try:
                medico = database.session.query(MedicoEntity).filter_by(cpf=cpf).first()
                if medico:
                    return MedicoDomain(
                        id=medico.id,
                        nome=medico.nome,
                        cpf=medico.cpf,
                        especialidade_id=medico.especialidade_id,
                        telefone=medico.telefone,
                        email=medico.email,
                        status=medico.status,
                        usuario_id=medico.usuario_id
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    def findByEmail(self, email:str)-> MedicoDomain:
        try:
            with BDConnectionHandler() as database:
                medico = database.session.query(MedicoEntity).filter_by(email=email).first()
                if medico:
                    return  MedicoDomain(
                        id=medico.id,
                        nome=medico.nome,
                        cpf=medico.cpf,
                        especialidade_id=medico.especialidade_id,
                        telefone=medico.telefone,
                        email=medico.email,
                        status=medico.status,
                        usuario_id=medico.usuario_id
                    )
                return None
        except Exception as e:
            raise e