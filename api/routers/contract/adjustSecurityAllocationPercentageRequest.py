from pydantic import BaseModel

class AdjustSecurityAllocationPercentageRequest(BaseModel):

    accountId : str
    securityId : str
    allocationPercentage : float