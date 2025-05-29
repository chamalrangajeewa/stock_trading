from pydantic import BaseModel

class AdjustAllocationAmountRequest(BaseModel):

    accountId : str
    allocationAmount : float