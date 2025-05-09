from datetime import datetime

from api.persistence.database import Database
from api.persistence.service import AccountEntity, TransactionEntity,SecuritySnapShotEntity
from sqlalchemy.orm import Session

class PurchaseSecurityCommand():
    
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


class PurchaseSecurityCommandHandler():

   _newAveragePerUnitCost:float = lambda self, currentAveragePerUnitCost, currentQuantity, quantityPurchased, costOfPurchase : ((currentAveragePerUnitCost * currentQuantity) + costOfPurchase)/(currentQuantity + quantityPurchased)

   def __init__(self, storageClient : Database) -> None:
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
            entity.netAmount = request.netAmount
            entity.date = request.date
            entity.description = request.description
            entity.externalId = request.externalId
            entity.newBalance = request.newBalance
            entity.settlementDate = request.settlementDate
            entity.accountId = accountEntity.id
            entity.type = "B"

            entity.quantity = request.quantity
            entity.perUnitCost = request.unitPrice
            entity.securityId = request.securityId
            entity.fees = request.fees
            accountEntity.fundBalance = accountEntity.fundBalance - entity.netAmount
            session.add(entity)

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(
                SecuritySnapShotEntity.accountId == accountEntity.id,
                SecuritySnapShotEntity.securityId == request.securityId).first()
            
            if not securitySnapShotEntity:
                securitySnapShotEntity = SecuritySnapShotEntity()
                securitySnapShotEntity.accountId = accountEntity.id
                securitySnapShotEntity.securityId = request.securityId              
                session.add(securitySnapShotEntity)

            securitySnapShotEntity.averagePerUnitCost = self._newAveragePerUnitCost(securitySnapShotEntity.averagePerUnitCost, securitySnapShotEntity.quantity, request.quantity, request.netAmount)
            securitySnapShotEntity.totalPurchaseFees += request.fees
            securitySnapShotEntity.totalPurchaseCost += request.netAmount
            securitySnapShotEntity.quantity += request.quantity
            securitySnapShotEntity.totalRealisedProfit += 0
            securitySnapShotEntity.totalSaleFees += 0
            securitySnapShotEntity.totalSaleIncome += 0  
            
            session.commit()

       return "OK"