from datetime import datetime
from ..persistence.database import Database
from ..persistence.service import SecurityEntity
from sqlalchemy.orm import Session
from pydantic import BaseModel

class SyncLivePriceCommand(BaseModel):
   securityId : str
   date : datetime
   unitPrice : float

class SyncLivePriceCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: SyncLivePriceCommand) -> str:
       with self._storageClient.session() as _session:
            session : Session = _session
            entity: SecurityEntity = session.query(SecurityEntity).filter(SecurityEntity.id == request.securityId).first()
            
            if not entity:
                return "OK"
                # raise Exception(f"securtyEntity not found,{request.securityId}")

            entity.livePerUnitCost = request.unitPrice
            session.commit()

       return "OK"


