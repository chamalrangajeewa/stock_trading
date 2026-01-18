from api.persistence.database import Database
from api.persistence.service import AccountEntity, SecuritySnapShotEntity
from sqlalchemy.orm import Session
from pydantic import BaseModel

class StocksplitCommand(BaseModel):
   externalAccountId : str
   securityId : str
   quantity : float

class StocksplitCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: StocksplitCommand) -> None:
       with self._storageClient.session() as _session:
            session : Session = _session
            accountEntity: AccountEntity = session.query(AccountEntity).filter(AccountEntity.externalId == request.externalAccountId).first()
            
            if not accountEntity:
                raise Exception("account not found")

            securitySnapShotEntity: SecuritySnapShotEntity = session.query(SecuritySnapShotEntity).filter(SecuritySnapShotEntity.securityId == request.securityId).first()
            
            newAveragePerUnitCost = (securitySnapShotEntity.averagePerUnitCost * securitySnapShotEntity.quantity) / (request.quantity)
            securitySnapShotEntity.quantity = request.quantity
            securitySnapShotEntity.averagePerUnitCost = newAveragePerUnitCost

            session.commit()