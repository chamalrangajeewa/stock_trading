from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select

from ..persistence.database import Database
from ..persistence.service import AccountEntity, SectorSnapShotEntity, TransactionEntity,SecuritySnapShotEntity, SecurityEntity

class SellSecurityCommand():

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

class SellSecurityCommandHandler():
    
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
           
            balance  = accountEntity.fundBalance + request.netAmount - request.newBalance 

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
            entity.type = "S"

            entity.quantity = request.quantity
            entity.perUnitCost = request.unitPrice
            entity.securityId = request.securityId
            entity.fees = request.fees
            accountEntity.fundBalance += entity.netAmount
            session.add(entity)

            security = session.execute(select(SecurityEntity).filter(SecurityEntity.id == request.securityId)).first()._t[0]
            stmt = select(SectorSnapShotEntity).filter(SectorSnapShotEntity.accountId == accountEntity.id).filter(SectorSnapShotEntity.sectorId == security.sectorId)
            sectorSnapshotEntity = session.execute(stmt).first()._t[0]

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(
                SecuritySnapShotEntity.sectorSnapshotId == sectorSnapshotEntity.id,
                SecuritySnapShotEntity.securityId == request.securityId).first()
            
            if not securitySnapShotEntity:
                raise Exception("no security snapshot found matching the filter")

            realisedProfitOrLoss = ((request.netAmount/request.quantity) - securitySnapShotEntity.averagePerUnitCost) * request.quantity
            entity.realisedProfit = realisedProfitOrLoss
            securitySnapShotEntity.quantity -= request.quantity
            securitySnapShotEntity.totalRealisedProfit += realisedProfitOrLoss
            securitySnapShotEntity.totalSaleFees += request.fees
            securitySnapShotEntity.totalSaleIncome += request.netAmount
            session.commit()

       return "OK"