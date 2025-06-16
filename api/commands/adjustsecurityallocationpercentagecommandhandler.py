from sqlalchemy import select
from api.persistence.database import Database
from api.persistence.service import AccountEntity, SecuritySnapShotEntity, SectorSnapShotEntity, SecurityEntity
from sqlalchemy.orm import Session, joinedload
from pydantic import BaseModel

class AdjustSecurityAllocationPercentageCommand(BaseModel):
   externalAccountId : str
   securityId : str
   allocationPercentage : int

class AdjustSecurityAllocationPercentageCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: AdjustSecurityAllocationPercentageCommand) -> None:
       with self._storageClient.session() as _session:
            session : Session = _session
            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == request.externalAccountId).first()
            
            if not accountEntity:
                raise Exception("account not found")
            
            stm = select(SecuritySnapShotEntity).options(
                joinedload(SecuritySnapShotEntity.sectorSnapshot)).where(SecuritySnapShotEntity.securityId == request.securityId).where(SectorSnapShotEntity.accountId == accountEntity.id)
            
            securitySnapshot : SecuritySnapShotEntity = session.scalars(stm).first()
            securitySnapshot.fundAllocationPercentage = request.allocationPercentage
            session.commit()