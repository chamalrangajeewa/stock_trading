from datetime import datetime
from decimal import Context, Decimal

from api.persistence.database import Database
from api.persistence.service import AccountEntity, SectorSnapShotEntity, TransactionEntity,SecuritySnapShotEntity, SecurityEntity
from sqlalchemy.orm import Session
from sqlalchemy import select

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
            
            balance  = accountEntity.fundBalance - request.netAmount - request.newBalance 

            if (round(balance)) != 0:
                raise Exception(f"the account balance does not match up. {accountEntity.fundBalance} {request.netAmount} {request.newBalance} {(accountEntity.fundBalance - request.netAmount)}")
           
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
            accountEntity.fundBalance -= entity.netAmount
            session.add(entity)

            security = session.execute(select(SecurityEntity).filter(SecurityEntity.id == request.securityId)).first()._t[0]
            stmt = select(SectorSnapShotEntity).filter(SectorSnapShotEntity.accountId == accountEntity.id).filter(SectorSnapShotEntity.sectorId == security.sectorId)
            sectorSnapshotEntity = session.execute(stmt).first()._t[0]

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(
                SecuritySnapShotEntity.sectorSnapshotId == sectorSnapshotEntity.id,
                SecuritySnapShotEntity.securityId == request.securityId).first()
            
            if not securitySnapShotEntity:
                securitySnapShotEntity = SecuritySnapShotEntity()
                securitySnapShotEntity.sectorSnapshotId = sectorSnapshotEntity.id
                securitySnapShotEntity.securityId = request.securityId              
                session.add(securitySnapShotEntity)

            newAverageUnitCost = self._newAveragePerUnitCost(securitySnapShotEntity.averagePerUnitCost, securitySnapShotEntity.quantity, request.quantity, request.netAmount)
            entity.averagePerUnitCost = newAverageUnitCost
            securitySnapShotEntity.averagePerUnitCost = newAverageUnitCost
            securitySnapShotEntity.totalPurchaseFees += request.fees
            securitySnapShotEntity.totalPurchaseCost += request.netAmount
            securitySnapShotEntity.quantity += request.quantity
            securitySnapShotEntity.totalRealisedProfit += 0
            securitySnapShotEntity.totalSaleFees += 0
            securitySnapShotEntity.totalSaleIncome += 0  
            
            session.commit()

       return "OK"