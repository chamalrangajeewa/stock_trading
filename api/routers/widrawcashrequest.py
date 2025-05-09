from pydantic import BaseModel
from datetime import datetime

class WidrawCashRequest(BaseModel):
    accountId : str
    netAmount : float
    externalTransactionId : str
    transactionDate: datetime
    description : str
    newBalance : float
    settlementDate : datetime