from typing import Dict
from src.domain.usecases.paciente.insert_paciente import PacienteInsertUseCase as PacienteInsertInterface
from src.data.interfaces.paciente_interface_repository import PacienteRepositoryInterface 
from src.domain.models.paciente_model import Paciente
from src.data.interfaces.endereco_interface_repository import EnderecoRepositoryInterface
from src.data.interfaces.convenio_interface_repository import ConvenioRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
import re 
class PacienteInsertUseCase(PacienteInsertInterface):
    def __init__(self, paciente_repository: PacienteRepositoryInterface,endereco_repository=EnderecoRepositoryInterface,convenio_repository=ConvenioRepositoryInterface):
        self.paciente_repository = paciente_repository
        self.endereco_repository = endereco_repository
        self.convenio_repository = convenio_repository
    def insert(self, paciente: Paciente) -> Dict:
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
        self.__insert_paciente(
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
    def __insert_paciente(self,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,contato_emergencia:str,alergia:str,endereco_id:int,convenio_id:int)-> None:
        self.paciente_repository.insert_paciente(
            alergia=alergia,
            contato_emergencia=contato_emergencia,
            convenio_id=convenio_id,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco_id=endereco_id,
            nome=nome,
            sexo=sexo,
            telefone= telefone
        )
        return None
    def __format_response(self,nome:str,cpf:str,data_nascimento:str,sexo:str,telefone:str,contato_emergencia:str,alergia:str,endereco_id:int,convenio_id:int) -> Dict:
        response = {
            "type": "Paciente",
            "attributes": {
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