import datetime
from typing import Any, Self
import pytest
from sqlalchemy import Connection
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from api.persistence import database
from api.persistence.service import TransactionEntity

from ..commands import DepositCashCommandHandler, DepositCashCommand
from ..persistence import Database

class TestDepositCashCommandHandler:
    
    @pytest.fixture()
    def get_database(self) -> Database:
        connection_url : str = "sqlite:///:memory:"
        return Database(connection_url)
    
    @pytest.fixture()
    def load_static_data(self, database : Database) -> Database:
        with database._engine.connect() as _connection:
            connection : Connection = _connection
            stm = text("""INSERT INTO sector (id, name) 
                        VALUES 
                        (1, 'Energy')
                        ,(2, 'Materials')
                        ,(3, 'Capital Goods')
                        ,(4, 'Commercial & Professional Services')
                        ,(5, 'Transportation')
                        ,(6, 'Automobiles & Components')
                        ,(7, 'Consumer Durables & Apparel')
                        ,(8, 'Consumer Services')
                        ,(9, 'Retailing')
                        ,(10, 'Food & Staples Retailing')
                        ,(11, '"Food, Beverage & Tobacco"')
                        ,(12, 'Household & Personal Products')
                        ,(13, 'Health Care Equipment & Services')
                        ,(14, 'Banks')
                        ,(15, 'Diversified Financials')
                        ,(16, 'Insurance')
                        ,(17, 'Software & Services')
                        ,(18, 'Telecommunication Services')
                        ,(19, 'Utilities')
                        ,(20, 'Real Estate Management&Development')""")
        
            connection.execute(stm)
            connection.commit()

    @classmethod
    def setup_class(cls) -> Any:

        connection_url : str = "sqlite:///:memory:"
        database = Database(connection_url)
        with database._engine.connect() as _connection:
            connection : Connection = _connection
            stm = text("""INSERT INTO sector (id, name) 
                        VALUES 
                        (1, 'Energy')
                        ,(2, 'Materials')
                        ,(3, 'Capital Goods')
                        ,(4, 'Commercial & Professional Services')
                        ,(5, 'Transportation')
                        ,(6, 'Automobiles & Components')
                        ,(7, 'Consumer Durables & Apparel')
                        ,(8, 'Consumer Services')
                        ,(9, 'Retailing')
                        ,(10, 'Food & Staples Retailing')
                        ,(11, '"Food, Beverage & Tobacco"')
                        ,(12, 'Household & Personal Products')
                        ,(13, 'Health Care Equipment & Services')
                        ,(14, 'Banks')
                        ,(15, 'Diversified Financials')
                        ,(16, 'Insurance')
                        ,(17, 'Software & Services')
                        ,(18, 'Telecommunication Services')
                        ,(19, 'Utilities')
                        ,(20, 'Real Estate Management&Development')""")
        
            connection.execute(stm)

            stm = text("""INSERT INTO account (id, external_id, fund_balance, investment) 
                        VALUES 
                        (1, 'CAS/104948-LI/0', 0, 1000000)""")

            connection.execute(stm)
            connection.commit()


    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """

    
    def test_handler_creation(self):
        handler: DepositCashCommandHandler = DepositCashCommandHandler(None)
        assert isinstance(handler, DepositCashCommandHandler)

    @pytest.mark.asyncio(loop_scope="function")
    async def test_handle_cashdepositcommand_throw_error_with_incorrect_accountId(self, get_database):
        
        handler: DepositCashCommandHandler = DepositCashCommandHandler(get_database)
        command: DepositCashCommand = DepositCashCommand()
        command.externalAccountId = "007"

        with pytest.raises(Exception) as excinfo:
            await handler.handle(command)
        assert excinfo.type is Exception


    @pytest.mark.asyncio(loop_scope="function")
    async def test_handle_cashdepositcommand_should_get_saved(self, get_database):
        
        handler: DepositCashCommandHandler = DepositCashCommandHandler(get_database)
        command: DepositCashCommand = DepositCashCommand()
        command.externalAccountId = "CAS/104948-LI/0"
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = "trx_external"
        command.description = "cashdeposit"
        command.amount = 1000
        command.balance = 1000
        command.settlementDate = datetime.datetime(2020, 5, 17)

        await handler.handle(command)

        # entity : TransactionEntity = None
        with get_database.session() as _session:
            session : Session = _session
            entity = session.query(TransactionEntity).filter(
                TransactionEntity.externalId == command.externalId).first()
        
        assert entity.externalId == command.externalId