from datetime import datetime
from api.persistence.database import Database
from api.persistence.service import AccountEntity, TransactionEntity
from sqlalchemy.orm import Session
from pydantic import BaseModel

class DepositCashCommand():
   externalAccountId : str
   externalId : str
   date : datetime
   netAmount : float
   description : str
   newBalance : str
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
            
            balance  = (accountEntity.fundBalance + request.netAmount) - request.newBalance

            if (round(balance)) != 0:
                raise Exception(f"the account balance does not match up. {accountEntity.fundBalance} {request.netAmount} {request.newBalance} {(accountEntity.fundBalance + request.netAmount)}")
       
            entity = TransactionEntity()
            entity.netAmount = request.netAmount
            entity.date = request.date
            entity.description = request.description
            entity.externalId = request.externalId
            entity.newBalance = request.newBalance
            entity.settlementDate = request.settlementDate
            entity.accountId = accountEntity.id
            entity.fees = 0
            entity.type = "R"

            entity.quantity = 0
            entity.perUnitCost = 0
            entity.securityId = None

            accountEntity.fundBalance += entity.netAmount
            session.add(entity)
            session.commit()

       return "OK"


