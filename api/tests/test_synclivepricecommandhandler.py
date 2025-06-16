from datetime import datetime
import pytest
from sqlalchemy import Connection
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from ..persistence.service import TransactionEntity

from ..commands.synclivepricecommandhandlera import SyncLivePriceCommandHandler, SyncLivePriceCommand
from ..persistence import Database

class TestSyncLivePriceUpdateCommandHandler:
    
    EXTERNAL_ACCOUNT_ID:str = "CAS/104948-LI/0" 

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

            stm = text("""INSERT INTO sectorsnapshot (account_id, sector_id, fund_allocation_percentage) 
                        VALUES 
                        (1, 15, 10)
                        ,(1, 16, 10)
                        ,(1, 1, 10)
                        ,(1, 14, 10)
                        ,(1, 3, 10)
                        ,(1, 2, 10)""")

            connection.execute(stm)

            stm = text("""INSERT INTO security (id, name, sector_id, live_per_unit_cost)
                          VALUES 
                          ('AAF.N0000', 'ASIA ASSET FINANCE PLC', 15,10)
                          ,('AAIC.N0000', 'SOFTLOGIC LIFE INSURANCE PLC', 16,10)
                          ,('ABAN.N0000', 'ABANS ELECTRICALS PLC', 1,10)
                          ,('ABL.N0000', 'AMANA BANK PLC', 14,10)
                          ,('ACAP.N0000', 'ASIA CAPITAL PLC', 15,10)
                          ,('ACL.N0000', 'ACL CABLES PLC', 3,10)
                          ,('ACME.N0000', 'ACME PRINTING & PACKAGING PLC', 2,10)""")

            connection.execute(stm)

            connection.commit()

        return database
    
    @pytest.fixture(scope="function")
    def handler(self, database: Database) -> SyncLivePriceCommandHandler:
        handler: SyncLivePriceCommandHandler = SyncLivePriceCommandHandler(database)
        return handler

    @pytest.fixture(scope="function")
    def command(self) -> SyncLivePriceCommand:
        command: SyncLivePriceCommand = SyncLivePriceCommand(securityId="COCR.N0000", unitPrice=100, date = datetime.now())
        return command

    def test_handler_creation(self):
        handler: SyncLivePriceCommandHandler = SyncLivePriceCommandHandler(None)
        assert isinstance(handler, SyncLivePriceCommandHandler)

    @pytest.mark.asyncio(loop_scope="function")
    async def test_invalid_account_cashdepositcommand_throw_error(self, handler: SyncLivePriceCommandHandler, command: SyncLivePriceCommand):
        
        command.externalAccountId = "007"

        with pytest.raises(Exception) as excinfo:
            await handler.handle(command)
        assert excinfo.type is Exception


    @pytest.mark.asyncio(loop_scope="function")
    async def test_(self,database :Database,  handler: SyncLivePriceCommandHandler,command: SyncLivePriceCommand):
         
        g =  await handler.handle(command)

        with database.session() as _session:
            session : Session = _session
            entity = session.query(TransactionEntity).filter(
                TransactionEntity.externalId == command.externalAccountId).first()
        
        assert entity.externalId == command.externalId