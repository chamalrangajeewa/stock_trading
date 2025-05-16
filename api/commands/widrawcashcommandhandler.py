from datetime import datetime
from sqlalchemy.orm import Session

from ..persistence.database import Database
from ..persistence.service import AccountEntity, TransactionEntity

class WidrawCashCommand:
  
   externalAccountId : str
   externalId : str
   date : datetime
   netAmount : float
   description : str
   newBalance : str
   settlementDate : datetime

class WidrawCashCommandHandler():

    def __init__(self, storageClient : Database):
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
            entity.netAmount = request.netAmount
            entity.date = request.date
            entity.description = request.description
            entity.externalId = request.externalId
            entity.newBalance = request.newBalance
            entity.settlementDate = request.settlementDate
            entity.accountId = accountEntity.id
            entity.type = "D"

            entity.quantity = 0
            entity.perUnitCost = 0
            entity.securityId = None

            accountEntity.fundBalance -= entity.netAmount
            session.add(entity)
            session.commit()

       return "OK"