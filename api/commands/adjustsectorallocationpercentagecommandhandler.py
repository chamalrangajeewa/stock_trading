from api.persistence.database import Database
from api.persistence.service import AccountEntity
from sqlalchemy.orm import Session
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

            session.commit()


