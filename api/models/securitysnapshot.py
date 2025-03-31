from pydantic import BaseModel
from datetime import datetime

class SecuritySnapshot(BaseModel):
    name : str
    externalId : str
    
    purchasedQuatity : int
    rollingAveragePurchaseUnitPrice : float    
    rollingPurchaseCommission : float
    rollingPurchaseCost : float
    
    soldQuantity : int
    rollingAverageSaleUnitPrice : float
    rollingSaleCommision : float
    rollingSaleProceeds : float

    holdingQuantity : int
    currentMarketPrice : float
    commissionUnrealised : float
    saleProceedsUnrealised : float 
    profitOrLossUnrealised : float
    
    profitOrLossRealised : float
    percentageAllocation : float

class PurchaseSnapshot(BaseModel):
    externalId : str
    quantity : int
    rollingAverageUnitPrice : float    
    rollingCommission : float
    rollingCost : float

class SaleSnapshot(BaseModel):
    externalId : str
    quantity : int
    rollingAverageUnitPrice : float
    rollingCommision : float
    rollingProceeds : float