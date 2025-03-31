from datetime import datetime
from pydantic import BaseModel

class TransactionCreateCommand(BaseModel):
    
    def __init__(self, _externalId : str, _date : datetime, _securityId : str, _quantity : int, _unitPrice : float, _cost : float):
     self.externalId = _externalId
     self.date = _date
     self.securityId  = _securityId
     self.quantity = _quantity
     self.unitPrice = _unitPrice
     self.cost = _cost

    externalId : str
    date : datetime
    securityId : str
    quantity : int
    price : float
    cost : float    

