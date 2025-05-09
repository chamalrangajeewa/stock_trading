from datetime import datetime
from pydantic import BaseModel

from api.persistence.database import Database
from api.persistence.service import SecuritySnapShotEntity, databaseService
from api.persistence.service import AccountEntity, TransactionEntity, databaseService
from sqlalchemy.orm import Session

class PurchaseSecurityCommand(BaseModel):
    
    securityId : str
    quantity : int
    unitPrice : float
    commission : float    
    externalAccountId : str
    externalId : str
    date : datetime
    amount : float
    description : str
    balance : str
    settlementDate : datetime


class PurchaseSecurityCommandHandler():

   _newAveragePerUnitCost:float = lambda currentAveragePerUnitCost, currentQuantity, quantityPurchased, costOfPurchase : ((currentAveragePerUnitCost * currentQuantity) + costOfPurchase)/(currentQuantity + quantityPurchased)

   def __init__(self, databaseService : databaseService, storageClient : Database):
       self._databaseService = databaseService
       self._storageClient = storageClient       

   async def handle(self, request: PurchaseSecurityCommand) -> str:
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
            entity.type = "B"

            entity.quantity = request.quantity
            entity.perUnitCost = request.unitPrice
            entity.securityId = request.securityId
            entity.commission = request.amount-(request.unitPrice * request.quantity)
            accountEntity.fundBalance = accountEntity.fundBalance - entity.amount
            session.add(entity)

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(
                SecuritySnapShotEntity.accountId == accountEntity.id,
                SecuritySnapShotEntity.securityId == request.securityId).first()
            
            if not securitySnapShotEntity:
                securitySnapShotEntity = SecuritySnapShotEntity()
                securitySnapShotEntity.accountId = accountEntity.id
                securitySnapShotEntity.securityId = request.securityId
                securitySnapShotEntity.averagePerUnitCost = self._newAveragePerUnitCost(0, 0, request.quantity, request.amount)
                securitySnapShotEntity.totalPurchaseCommission += request.commission
                securitySnapShotEntity.totalPurchaseCost += request.amount
                securitySnapShotEntity.totalQuantity += request.quantity
                securitySnapShotEntity.totalRealisedProfit += 0
                securitySnapShotEntity.totalSaleCommission += 0
                securitySnapShotEntity.totalSaleIncome += 0  
                session.add(securitySnapShotEntity)

            securitySnapShotEntity.averagePerUnitCost = self._newAveragePerUnitCost(securitySnapShotEntity.averagePerUnitCost, securitySnapShotEntity.totalQuantity, request.quantity, request.amount)
            securitySnapShotEntity.totalPurchaseCommission += request.commission
            securitySnapShotEntity.totalPurchaseCost += request.amount
            securitySnapShotEntity.totalQuantity += request.quantity
            securitySnapShotEntity.totalRealisedProfit += 0
            securitySnapShotEntity.totalSaleCommission += 0
            securitySnapShotEntity.totalSaleIncome += 0  
            
            session.commit()

       return await self._databaseService.process()