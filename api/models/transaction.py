from datetime import datetime
from pydantic import BaseModel

class AccountSnapshot:
   externalAccountId : str
   investmentTotal : float
   investmentCommitted : float
   cashBalance : float
   gains : float

class PurchaseTransaction(BaseModel):
    
    def __init__(self, _externalId : str, _date : datetime, _securityId : str, _quantity : int, _price : float, _cost : float):
     self.externalId = _externalId
     self.date = _date
     self.securityId  = _securityId
     self.quantity = _quantity
     self.unitPrice = _price
     self.commission = _cost

    externalId : str
    date : datetime
    securityId : str
    quantity : int
    price : float
    cost : float    


class SaleTransaction(BaseModel):
    
    def __init__(self, _externalId : str, _date : datetime, _securityId : str, _quantity : int, _price : float, _cost : float):
     self.externalId = _externalId
     self.date = _date
     self.securityId  = _securityId
     self.quantity = _quantity
     self.unitPrice = _price
     self.commission = _cost

    externalId : str
    date : datetime
    securityId : str
    quantity : int
    price : float
    cost : float    