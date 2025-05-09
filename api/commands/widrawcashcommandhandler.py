from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.persistence.database import Database
from api.persistence.service import AccountEntity, TransactionEntity, databaseService

class WidrawCashCommand:
  
   externalAccountId : str
   externalId : str
   date : datetime
   amount : float
   description : str
   balance : str
   settlementDate : datetime

class WidrawCashCommandHandler():

    def __init__(self, databaseService : databaseService, storageClient : Database):
       self._databaseService = databaseService
       self._storageClient = storageClient          

    async def handle(self, request: WidrawCashCommand) -> str:
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
            entity.amount = request.amount
            entity.date = request.date
            entity.description = request.description
            entity.externalId = request.externalId
            entity.balance = request.balance
            entity.settlementDate = request.settlementDate
            entity.accountId = accountEntity.id
            entity.type = "D"

            entity.quantity = 0
            entity.perUnitCost = 0
            entity.securityId = None

            accountEntity.fundBalance -= entity.amount
            session.add(entity)
            session.commit()

       return await self._databaseService.process()