import datetime
import pytest
from sqlalchemy import Connection
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from api.persistence import database
from api.persistence.service import TransactionEntity

from ..commands import DepositCashCommandHandler, DepositCashCommand
from ..persistence import Database

class TestDepositCashCommandHandler:
    
    @pytest.fixture(scope="class")
    def database(self) -> Database:
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

            stm = text("""INSERT INTO security (id, name, sectorId)
                          VALUES 
                          ('AAF.N0000', 'ASIA ASSET FINANCE PLC', 15)
                          ,('AAIC.N0000', 'SOFTLOGIC LIFE INSURANCE PLC', 16)
                          ,('ABAN.N0000', 'ABANS ELECTRICALS PLC', 1)
                          ,('ABL.N0000', 'AMANA BANK PLC', 14)
                          ,('ACAP.N0000', 'ASIA CAPITAL PLC', 15)
                          ,('ACL.N0000', 'ACL CABLES PLC', 3)
                          ,('ACME.N0000', 'ACME PRINTING & PACKAGING PLC', 2)""")

            connection.execute(stm)

            connection.commit()

        return database
    
    @pytest.fixture(scope="function")
    def handler(self, database: Database) -> DepositCashCommandHandler:
        handler: DepositCashCommandHandler = DepositCashCommandHandler(database)
        return handler

    @pytest.fixture(scope="function")
    def command(self) -> DepositCashCommand:
        command: DepositCashCommand = DepositCashCommand()
        command.externalAccountId = "CAS/104948-LI/0"
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = "trx_external"
        command.description = "cashdeposit"
        command.netAmount = 1000
        command.newBalance = 1000
        command.settlementDate = datetime.datetime(2020, 5, 17)
        return command

    def test_handler_creation(self):
        handler: DepositCashCommandHandler = DepositCashCommandHandler(None)
        assert isinstance(handler, DepositCashCommandHandler)

    @pytest.mark.asyncio(loop_scope="function")
    async def test_invalid_account_cashdepositcommand_throw_error(self, handler: DepositCashCommandHandler, command: DepositCashCommand):
        
        command.externalAccountId = "007"

        with pytest.raises(Exception) as excinfo:
            await handler.handle(command)
        assert excinfo.type is Exception


    @pytest.mark.asyncio(loop_scope="function")
    async def test_duplicate_cashdepositcommand_throw_error(self, handler: DepositCashCommandHandler, command: DepositCashCommand):
        
        await handler.handle(command)

        with pytest.raises(Exception) as excinfo:
            await handler.handle(command)
        assert excinfo.type is Exception


    @pytest.mark.asyncio(loop_scope="function")
    async def test_valid_cashdepositcommand_should_get_saved(self,database :Database,  handler: DepositCashCommandHandler,command: DepositCashCommand):
        
        command.externalId = "unique"
        await handler.handle(command)

        with database.session() as _session:
            session : Session = _session
            entity = session.query(TransactionEntity).filter(
                TransactionEntity.externalId == command.externalId).first()
        
        assert entity.externalId == command.externalId