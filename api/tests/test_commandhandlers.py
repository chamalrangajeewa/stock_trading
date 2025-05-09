import datetime
from typing import List
import pytest
from sqlalchemy import Connection
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from ..persistence.service import AccountEntity, SecuritySnapShotEntity, TransactionEntity
from ..commands import DepositCashCommandHandler, DepositCashCommand,WidrawCashCommandHandler, WidrawCashCommand, PurchaseSecurityCommandHandler,PurchaseSecurityCommand, SellSecurityCommandHandler, SellSecurityCommand
from ..persistence import Database

class TestCommandHandler:
    
    EXTERNAL_ACCOUNT_ID:str = "CAS/104948-LI/0"
    # def __init__(self)-> None:
    #     pass       

    def defaultDepositCashCommand(self, externalId:str, amount:float = 0, balance:float = 0) -> DepositCashCommand:
        command: DepositCashCommand = DepositCashCommand()
        command.externalAccountId = self.EXTERNAL_ACCOUNT_ID
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = externalId
        command.description = DepositCashCommand.__name__
        command.netAmount = amount
        command.newBalance = balance
        command.settlementDate = datetime.datetime(2020, 5, 17)
        return command
    
    def defaultWidrawCashCommand(self, externalId:str, amount:float = 0, balance:float = 0) -> WidrawCashCommand:
        command: WidrawCashCommand = WidrawCashCommand()
        command.externalAccountId = self.EXTERNAL_ACCOUNT_ID
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = externalId
        command.description = WidrawCashCommand.__name__
        command.netAmount = amount
        command.newBalance = balance
        command.settlementDate = datetime.datetime(2020, 5, 17)
        return command
    
    def defaultPurchaseSecurityCommand(self, externalId:str, securityId:str, unitPrice:float = 1, quantity:int = 10, amount:float = 0, balance:float = 0) -> PurchaseSecurityCommand:
        command: PurchaseSecurityCommand = PurchaseSecurityCommand()
        command.externalAccountId = self.EXTERNAL_ACCOUNT_ID
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = externalId
        command.description = PurchaseSecurityCommand.__name__
        command.netAmount = amount
        command.newBalance = balance
        command.settlementDate = datetime.datetime(2020, 5, 17)
        command.securityId = securityId
        command.quantity = quantity
        command.unitPrice = unitPrice
        command.fees = amount * 0.0112
        return command
    
    def defaultSellSecurityCommand(self, externalId:str, securityId:str, unitPrice:float = 1, quantity:int = 10, amount:float = 0, balance:float = 0) -> SellSecurityCommand:
        command: SellSecurityCommand = SellSecurityCommand()
        command.externalAccountId = self.EXTERNAL_ACCOUNT_ID
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = externalId
        command.description = SellSecurityCommand.__name__
        command.netAmount = amount
        command.newBalance = balance
        command.settlementDate = datetime.datetime(2020, 5, 17)
        command.securityId = securityId
        command.quantity = quantity
        command.unitPrice = unitPrice
        command.fees = amount * 0.0112
        return command

    @pytest.fixture(scope="function")
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
    def handlers(self, database: Database) -> dict:

        handlers = dict()    
        handlers[DepositCashCommand.__name__] = DepositCashCommandHandler(database)
        handlers[WidrawCashCommand.__name__] = WidrawCashCommandHandler(database)
        handlers[PurchaseSecurityCommand.__name__] = PurchaseSecurityCommandHandler(database)
        handlers[SellSecurityCommand.__name__] = SellSecurityCommandHandler(database)

        return handlers

    @pytest.fixture(scope="function")
    def command(self) -> DepositCashCommand:
        command: DepositCashCommand = DepositCashCommand()
        command.externalAccountId = "CAS/104948-LI/0"
        command.date = datetime.datetime(2020, 5, 17)
        command.externalId = "trx_external"
        command.description = "cashdeposit"
        command.amount = 1000
        command.balance = 1000
        command.settlementDate = datetime.datetime(2020, 5, 17)
        return command

    
    @pytest.mark.asyncio(loop_scope="function")
    async def test_command_sequence(self, handlers: dict, database: Database) -> None:
        
        commands = [
            self.defaultDepositCashCommand(1,amount=10000), 
            self.defaultPurchaseSecurityCommand(2,'AAF.N0000', unitPrice=10, quantity=100, balance=9000),
            self.defaultSellSecurityCommand(3,'AAF.N0000', unitPrice=15, quantity=100, balance=9000),
            self.defaultWidrawCashCommand(4,amount=1000), 
            ]

        for x in commands:
            await handlers[x.__class__.__name__].handle(x)
        

        with database.session() as _session:
            session : Session = _session
            
            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == self.EXTERNAL_ACCOUNT_ID).first()                                 

            transactions: List[TransactionEntity] = session.query(TransactionEntity).filter(
                TransactionEntity.accountId == accountEntity.id).all()

            securitySnapShots: List[SecuritySnapShotEntity] = session.query(SecuritySnapShotEntity).filter(SecuritySnapShotEntity.accountId == accountEntity.id).all()                                 

        securitySnapShots[0].averagePerUnitCost = 0
        securitySnapShots[0].quantity = 0
        securitySnapShots[0].totalPurchaseCost = 0
        securitySnapShots[0].totalPurchaseFees = 0
        securitySnapShots[0].totalRealisedProfit = 0
        securitySnapShots[0].totalSaleFees = 0
        securitySnapShots[0].totalSaleIncome = 0
        accountEntity.fundBalance = 0

        assert len(securitySnapShots) == 1
        assert len(transactions) == len(commands)
        