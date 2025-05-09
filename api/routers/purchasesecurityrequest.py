from datetime import datetime
from pydantic import BaseModel

class PurchaseSecurityRequest(BaseModel):

    accountId : str
    netAmount : float
    externalTransactionId : str
    transactionDate: datetime
    description : str
    newBalance : float
    settlementDate : datetime
    securityId : str
    quantity : int
    unitPrice : float
    fees : float