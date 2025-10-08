from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface
from src.domain.models.paciente_model import Paciente as PacienteDomain
from src.infra.db.entities.paciente import Paciente as PacienteEntity
class PacienteRepository(PacienteRepositoryInterface):
    @classmethod
    def insert_paciente(cls,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,alergia:str,contato_emergencia:str,endereco_id:int,convenio_id:int,usuario_id:int) -> None:
        with BDConnectionHandler() as database:
            try:
                paciente = PacienteEntity(
                    nome=nome,
                    cpf=cpf,
                    data_nascimento=data_nascimento,
                    sexo=sexo,
                    telefone=telefone,
                    alergia=alergia,
                    contato_emergencia=contato_emergencia,
                    endereco_id=endereco_id,
                    convenio_id=convenio_id,
                    usuario_id=usuario_id
                )
                database.session.add(paciente)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    def select_paciente(cls, id: int) -> PacienteDomain:
        with BDConnectionHandler() as database:
            try:
                paciente = database.session.query(PacienteEntity).filter_by(id=id).first()
                if paciente:
                    return PacienteDomain(
                        id=paciente.id,
                        nome=paciente.nome,
                        data_nascimento=paciente.data_nascimento,
                        cpf=paciente.cpf,
                        sexo=paciente.sexo,
                        telefone=paciente.telefone,
                        alergia=paciente.alergia,
                        contato_emergencia=paciente.contato_emergencia,
                        endereco_id=paciente.endereco_id,
                        convenio_id=paciente.convenio_id,
                        usuario_id=paciente.usuario_id
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    def update_paciente(cls, id: int, nome: str, cpf: str, data_nascimento: str, sexo: str, telefone: str, alergia: str, contato_emergencia: str, endereco_id: int, convenio_id: int,usuario_id:int) -> None:
        with BDConnectionHandler() as database:
            try:
                paciente = database.session.query(PacienteEntity).filter_by(id=id).first()
                if paciente:
                    paciente.nome = nome
                    paciente.cpf = cpf
                    paciente.data_nascimento = data_nascimento
                    paciente.sexo = sexo
                    paciente.telefone = telefone
                    paciente.alergia = alergia
                    paciente.contato_emergencia = contato_emergencia
                    paciente.endereco_id = endereco_id
                    paciente.convenio_id = convenio_id
                    paciente.usuario_id = usuario_id
                    database.session.commit()
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    def delete_paciente(cls,id:int)->bool:
        with BDConnectionHandler() as database:
            try:
                paciente = database.session.query(PacienteEntity).filter_by(id=id).first()
                if paciente:
                    database.session.delete(paciente)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    def list_pacientes(cls) -> List[PacienteDomain]:
        with BDConnectionHandler() as database:
            try:
                pacientes = database.session.query(PacienteEntity).all()
                return [
                    PacienteDomain(
                        id=paciente.id,
                        nome=paciente.nome,
                        data_nascimento=paciente.data_nascimento,
                        cpf=paciente.cpf,
                        sexo=paciente.sexo,
                        telefone=paciente.telefone,
                        alergia=paciente.alergia,
                        contato_emergencia=paciente.contato_emergencia,
                        endereco_id=paciente.endereco_id,
                        convenio_id=paciente.convenio_id,
                        usuario_id=paciente.usuario_id
                    ) for paciente in pacientes
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    def findByEmail(self, email:str)-> PacienteDomain:
        try:
            with BDConnectionHandler() as database:
                paciente = database.session.query(PacienteEntity).filter_by(email=email).first()
                if paciente:
                    return PacienteDomain(
                        id=paciente.id,
                        nome=paciente.nome,
                        data_nascimento=paciente.data_nascimento,
                        cpf=paciente.cpf,
                        sexo=paciente.sexo,
                        telefone=paciente.telefone,
                        alergia=paciente.alergia,
                        contato_emergencia=paciente.contato_emergencia,
                        endereco_id=paciente.endereco_id,
                        convenio_id=paciente.convenio_id,
                        usuario_id=paciente.usuario_id
                    )
                return None
        except Exception as e:
            raise e