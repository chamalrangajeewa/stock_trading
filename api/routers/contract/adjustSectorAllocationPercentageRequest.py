from pydantic import BaseModel

class AdjustSectorAllocationPercentageRequest(BaseModel):

    accountId : str
    name : str
    allocationPercentage : float