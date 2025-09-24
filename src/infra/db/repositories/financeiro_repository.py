from typing import List
from src.infra.db.settings.connection import BDConnectionHandler
from src.data.interfaces.financeiro_interface_repository import FinanceiroRepositoryInterface
from src.domain.models.financeiro_model import Financeiro as FinanceiroDomain
from src.infra.db.entities.financeiro import Financeiro as FinanceiroEntity

class FinanceiroRepository(FinanceiroRepositoryInterface):
    
    def create(self, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        with BDConnectionHandler() as database:
            try:
                financeiro = FinanceiroEntity(
                    paciente_id=paciente_id,
                    convenio_id=convenio_id,
                    valor=valor,
                    data_emissao=data_emisao,
                    data_vencimento=data_vencimento,
                    status_pagamento=status_pagamento
                )
                database.session.add(financeiro)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def update(self, id: int, paciente_id: int, convenio_id: int, valor: float, data_emisao: str, data_vencimento: str, status_pagamento: str) -> None:
        with BDConnectionHandler() as database:
            try:
                financeiro = database.session.query(FinanceiroEntity).filter_by(id=id).first()
                if financeiro:
                    financeiro.paciente_id = paciente_id
                    financeiro.convenio_id = convenio_id
                    financeiro.valor = valor
                    financeiro.data_emissao = data_emisao
                    financeiro.data_vencimento = data_vencimento
                    financeiro.status_pagamento = status_pagamento
                    database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
    
    def delete(self, id: int) -> bool:
        with BDConnectionHandler() as database:
            try:
                financeiro = database.session.query(FinanceiroEntity).filter_by(id=id).first()
                if financeiro:
                    database.session.delete(financeiro)
                    database.session.commit()
                    return True
                return False
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findById(self, id: int) -> FinanceiroDomain:
        with BDConnectionHandler() as database:
            try:
                financeiro = database.session.query(FinanceiroEntity).filter_by(id=id).first()
                if financeiro:
                    return FinanceiroDomain(
                        id=financeiro.id,
                        paciente_id=financeiro.paciente_id,
                        convenio_id=financeiro.convenio_id,
                        valor=financeiro.valor,
                        data_emissao=financeiro.data_emissao,
                        data_vencimento=financeiro.data_vencimento,
                        status_pagamento=financeiro.status_pagamento
                    )
                return None
            except Exception as e:
                database.session.rollback()
                raise e
    
    def findAll(self) -> List[FinanceiroDomain]:
        with BDConnectionHandler() as database:
            try:
                financeiros = database.session.query(FinanceiroEntity).all()
                return [
                    FinanceiroDomain(
                        id=financeiro.id,
                        paciente_id=financeiro.paciente_id,
                        convenio_id=financeiro.convenio_id,
                        valor=financeiro.valor,
                        data_emissao=financeiro.data_emissao,
                        data_vencimento=financeiro.data_vencimento,
                        status_pagamento=financeiro.status_pagamento
                    ) for financeiro in financeiros
                ]
            except Exception as e:
                database.session.rollback()
                raise e
