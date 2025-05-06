from datetime import datetime
from pydantic import BaseModel

from api.persistence.service import databaseService

class PurchaseSecurityCommand(BaseModel):
    
    def __init__(self, _externalId : str, _date : datetime, _securityId : str, _quantity : int, _unitPrice : float, _cost : float):
     self.externalId = _externalId
     self.date = _date
     self.securityId  = _securityId
     self.quantity = _quantity
     self.unitPrice = _unitPrice
     self.commission = _cost

    accountId : str
    externalId : str
    date : datetime
    securityId : str
    quantity : int
    unitPrice : float
    commission : float    


class PurchaseSecurityCommandHandler():
    
   def __init__(self, databaseService : databaseService):
       self._databaseService = databaseService       

   async def handle(self, request: PurchaseSecurityCommand) -> str:
       return await self._databaseService.process()