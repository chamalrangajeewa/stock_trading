from datetime import datetime
from sqlalchemy.orm import Session

from api.persistence.database import Database
from api.persistence.service import AccountEntity, SecuritySnapShotEntity, TransactionEntity, databaseService

class SellSecurityCommand():
    
    # def __init__(self, _externalId : str, _date : datetime, _securityId : str, _quantity : int, _unitPrice : float, _cost : float):
    #  self.externalId = _externalId
    #  self.date = _date
    #  self.securityId  = _securityId
    #  self.quantity = _quantity
    #  self.unitPrice = _unitPrice
    #  self.commission = _cost

    securityId : str
    quantity : int
    unitPrice : float
    fees : float    
    externalAccountId : str
    externalId : str
    date : datetime
    netAmount : float 
    description : str
    newBalance : float
    settlementDate : datetime

class SalesSecurityCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: SellSecurityCommand) -> str:
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
            entity.type = "S"

            entity.quantity = request.quantity
            entity.perUnitCost = request.unitPrice
            entity.securityId = request.securityId
            entity.fees = request.fees
            accountEntity.fundBalance += entity.netAmount
            session.add(entity)

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(
                SecuritySnapShotEntity.accountId == accountEntity.id,
                SecuritySnapShotEntity.securityId == request.securityId).first()
            
            if not securitySnapShotEntity:
                raise Exception("no security snapshot found matching the filter")

            securitySnapShotEntity.quantity -= request.quantity
            securitySnapShotEntity.totalRealisedProfit += (request.unitPrice - securitySnapShotEntity.averagePerUnitCost) * request.quantity
            securitySnapShotEntity.totalSaleFees += request.fees
            securitySnapShotEntity.totalSaleIncome += request.netAmount
            session.commit()

       return "OK"