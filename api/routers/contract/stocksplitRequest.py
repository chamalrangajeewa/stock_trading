from pydantic import BaseModel

class StocksplitRequest(BaseModel):

    accountId : str
    securityId : str
    quantity : float