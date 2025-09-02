from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.medicamento_interface_repository import MedicamentoRepositoryInterface
from src.domain.models.medicamento_model import Medicamento as MedicamentoDomain
from src.infra.db.entities.medicamento import Medicamento as MedicamentoEntity

class MedicamentoRepository(MedicamentoRepositoryInterface):
    
    def create(self, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        with BDConnectionHandler() as database:
            try:
                medicamento = MedicamentoEntity(
                    nome=nome,
                    descricao=descricao,
                    fabricante=fabricante,
                    validade=validade,
                    quantidade_estoque=quantidade_estoque
                )
                database.session.add(medicamento)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, nome: str, descricao: str, fabricante: str, validade: str, quantidade_estoque: int) -> None:
        with BDConnectionHandler() as database:
            try:
                medicamento = database.session.query(MedicamentoEntity).filter_by(id=id).first()
                if medicamento:
                    medicamento.nome = nome
                    medicamento.descricao = descricao
                    medicamento.fabricante = fabricante
                    medicamento.validade = validade
                    medicamento.quantidade_estoque = quantidade_estoque
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                medicamento = database.session.query(MedicamentoEntity).filter_by(id=id).first()
                if medicamento:
                    database.session.delete(medicamento)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> MedicamentoDomain:
        with BDConnectionHandler() as database:
            try:
                medicamento = database.session.query(MedicamentoEntity).filter_by(id=id).first()
                if medicamento:
                    return MedicamentoDomain(
                        id=medicamento.id,
                        nome=medicamento.nome,
                        descricao=medicamento.descricao,
                        fabricante=medicamento.fabricante,
                        validade=medicamento.validade,
                        quantidade_estoque=medicamento.quantidade_estoque
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[MedicamentoDomain]:
        with BDConnectionHandler() as database:
            try:
                medicamentos = database.session.query(MedicamentoEntity).all()
                return [
                    MedicamentoDomain(
                        id=medicamento.id,
                        nome=medicamento.nome,
                        descricao=medicamento.descricao,
                        fabricante=medicamento.fabricante,
                        validade=medicamento.validade,
                        quantidade_estoque=medicamento.quantidade_estoque
                    ) for medicamento in medicamentos
                ]
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findByNome(self, nome: str) -> MedicamentoDomain:
        with BDConnectionHandler() as database:
            try:
                medicamento = database.session.query(MedicamentoEntity).filter_by(nome=nome).first()
                if medicamento:
                    return MedicamentoDomain(
                        id=medicamento.id,
                        nome=medicamento.nome,
                        descricao=medicamento.descricao,
                        fabricante=medicamento.fabricante,
                        validade=medicamento.validade,
                        quantidade_estoque=medicamento.quantidade_estoque
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
