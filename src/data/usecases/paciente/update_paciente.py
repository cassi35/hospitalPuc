from typing import Dict
from src.domain.usecases.paciente.update_paciente import PacienteUpdateUseCase as PacienteUpdateInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface 
from src.infra.db.entities.paciente import Paciente
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
import re 
class PacienteUpdateUseCase(PacienteUpdateInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface):
        self.paciente_repository = paciente_repository

    def update(self, paciente_id: int, paciente: Paciente) -> Dict:
        self.__validade_informations(
            nome=paciente.nome,
            cpf=paciente.cpf,
            data_nascimento=paciente.data_nascimento,
            sexo=paciente.sexo,
            telefone=paciente.telefone,
            contato_emergencia=paciente.contato_emergencia,
            alergia=paciente.alergia,
            endereco_id=paciente.endereco_id,
            convenio_id=paciente.convenio_id
        )
        self.__paciente_exists(paciente_id=paciente_id)
        self.__update_paciente(
                paciente_id=paciente_id,
                nome=paciente.nome,
                cpf=paciente.cpf,
                data_nascimento=paciente.data_nascimento,
                sexo=paciente.sexo,
                telefone=paciente.telefone,
                contato_emergencia=paciente.contato_emergencia,
                alergia=paciente.alergia,
                endereco_id=paciente.endereco_id,
                convenio_id=paciente.convenio_id
        )
        response = self.__format_response(
            paciente_id=paciente_id,
            nome=paciente.nome,
            cpf=paciente.cpf,
            data_nascimento=paciente.data_nascimento,
            sexo=paciente.sexo,
            telefone=paciente.telefone,
            contato_emergencia=paciente.contato_emergencia,
            alergia=paciente.alergia,
            endereco_id=paciente.endereco_id,
            convenio_id=paciente.convenio_id
        )
        return response
    def __validade_informations(self,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,contato_emergencia:str,alergia:str,endereco_id:int,convenio_id:int)-> None:
        if not nome or nome.strip() == "" or len(nome) < 3 or len(nome) > 20:
            raise HttpBadRequestError("nome invalido")
        if not cpf or cpf.strip() == "" or len(cpf) != 11 or not cpf.isdigit():
            raise HttpBadRequestError("cpf invalido")
        if re.match(r'\d{4}-\d{2}-\d{2}',data_nascimento) is None:
            raise HttpBadRequestError("data de nascimento invalida")
        if sexo not in ['m','f']:
            raise HttpBadRequestError("sexo invalido")
        if not telefone or len(telefone) != 11 or not telefone.isdigit():
            raise HttpBadRequestError("telefone invalido")
        if not contato_emergencia or len(contato_emergencia) != 11 or not contato_emergencia.isdigit():
            raise HttpBadRequestError("contato emergencia invalido")

        if len(alergia) > 200:
            raise HttpBadRequestError("alergia invalida")
        endereco = self.endereco_repository.select_endereco(id=endereco_id)
        convenio = self.convenio_repository.select_convenio(id=convenio_id)
        if not endereco:
            raise HttpNotFoundError("endereco nao encontrado")
        if not convenio:
            raise HttpNotFoundError("convenio nao encontrado")
        return None
    def __paciente_exists(self,paciente_id:int) -> None:
        paciente = self.paciente_repository.select_paciente(id=paciente_id)
        if not paciente:
            raise HttpNotFoundError("paciente nao existe")
        return None
    def __update_paciente(self,paciente_id:int,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,contato_emergencia:str,alergia:str,endereco_id:int,convenio_id:int)-> None:
        self.paciente_repository.update_paciente(
            id=paciente_id,
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            sexo=sexo,
            telefone=telefone,
            contato_emergencia=contato_emergencia,
            alergia=alergia,
            endereco_id=endereco_id,
            convenio_id=convenio_id
        )
        return None
    def __format_response(self,paciente_id:int,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,contato_emergencia:str,alergia:str,endereco_id:int,convenio_id:int) -> Dict:
        response = {
            "type":"Paciente",
            "id": paciente_id,
            "attributes":{
                "nome": nome,
                "cpf": cpf,
                "data_nascimento": data_nascimento,
                "sexo": sexo,
                "telefone": telefone,
                "contato_emergencia": contato_emergencia,
                "alergia": alergia,
                "endereco_id": endereco_id,
                "convenio_id": convenio_id
            }
        } 
        return response