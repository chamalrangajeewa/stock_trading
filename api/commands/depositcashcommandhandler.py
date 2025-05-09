from datetime import datetime
from dependency_injector import containers, providers
from api.persistence.database import Database
from api.persistence.service import AccountEntity, TransactionEntity, databaseService
from sqlalchemy.orm import Session

class DepositCashCommand:
   externalAccountId : str
   externalId : str
   date : datetime
   amount : float
   description : str
   balance : str
   settlementDate : datetime

class DepositCashCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: DepositCashCommand) -> str:
       with self._storageClient.session() as _session:
            session : Session = _session
            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == request.externalAccountId).first()
            
            if not accountEntity:
                raise Exception("account not found")

            entity: TransactionEntity = session.query(TransactionEntity).filter(
                TransactionEntity.accountId == accountEntity.id,
                TransactionEntity.externalId == request.externalId).first()
            
            if entity:
                raise Exception("duplicate transaction")
           
            entity = TransactionEntity()
            entity.netAmount = request.amount
            entity.date = request.date
            entity.description = request.description
            entity.externalId = request.externalId
            entity.newBalance = request.balance
            entity.settlementDate = request.settlementDate
            entity.accountId = accountEntity.id
            entity.type = "R"

            entity.quantity = 0
            entity.perUnitCost = 0
            entity.securityId = None

            accountEntity.fundBalance += entity.netAmount
            session.add(entity)
            session.commit()

       return await "OK"


