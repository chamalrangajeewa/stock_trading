from sqlalchemy import select
from api.persistence.database import Database
from api.persistence.service import AccountEntity, SectorEntity, SectorSnapShotEntity
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel

class AdjustSectorAllocationPercentageCommand(BaseModel):
   externalAccountId : str
   sectorName : str
   allocationPercentage : float

class AdjustSectorAllocationPercentageCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: AdjustSectorAllocationPercentageCommand) -> None:
       with self._storageClient.session() as _session:
            session : Session = _session
            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == request.externalAccountId).first()
            
            if not accountEntity:
                raise Exception("account not found")

            sector = session.query(SectorEntity).filter(SectorEntity.name == request.sectorName).first()

            stm = select(SectorSnapShotEntity).where(SectorSnapShotEntity.sectorId == sector.id).where(SectorSnapShotEntity.accountId == accountEntity.id)
            
            sectorSnapshot : SectorSnapShotEntity = session.scalars(stm).first()
            sectorSnapshot.fundAllocationPercentage = request.allocationPercentage
            session.commit()