from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from ..persistence.database import Database
from ..persistence.service import AccountEntity, SecurityEntity, SecuritySnapShotEntity, TransactionEntity
from ..routers import AccountSnapshot, SectorSnapshot, SecuritySnapshot

class ViewDashboardCashCommand:
  
   externalAccountId : str
   

class ViewDashboardCommandHandler():

    def __init__(self, storageClient : Database):
       self._storageClient = storageClient          

    async def handle(self, request: ViewDashboardCashCommand) -> AccountSnapshot:
       with self._storageClient.session() as _session:
            session : Session = _session

            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == request.externalAccountId).first()
          
            if not accountEntity:
                raise Exception("account not found")


            stmt = select(SecurityEntity, SecuritySnapShotEntity).join_from(SecurityEntity, SecuritySnapShotEntity, SecurityEntity.id == SecuritySnapShotEntity.securityId).where(SecuritySnapShotEntity.accountId == accountEntity.id)
            print(stmt)    
            security_securitySnapshot_Tuple = session.execute(stmt).all()

            for o in security_securitySnapshot_Tuple:
                x, y = o.t[0].sectorId

            result: AccountSnapshot = AccountSnapshot()

            result.id = accountEntity.id
            result.allocationAmount = accountEntity.investment
            result.balanceAmount = accountEntity.fundBalance

            h = filter(lambda o: o.t[0].sectorId == 2, security_securitySnapshot_Tuple)
            
            for sectorSnapshotEntity in accountEntity.sectorSnapshots:
                sectorEntity = sectorSnapshotEntity.sector
                pair = filter(lambda o: o.t[0].sectorId == sectorEntity.id, security_securitySnapshot_Tuple)
                
                sector:SectorSnapshot = SectorSnapshot(
                    name = sectorEntity.name,
                    allocationPercentage = sectorSnapshotEntity.fundAllocationPercentage                     
                )


                result.sectors.append(sector)


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

       return result