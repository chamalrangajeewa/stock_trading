from typing import List
from pydantic import BaseModel

class SecuritySnapshot(BaseModel):

    name : str
    id : str    
    allocationPercentage: float
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float
    quantity : float
    averagePerUnitCost : float
    livePerUnitCost : float


class SectorSnapshot(BaseModel):

    name : str
    securities : List[SecuritySnapshot] = list()
    allocationPercentage: float
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float


class AccountSnapshot(BaseModel):
    
    id : str
    owner : str
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float
    sectors : List[SectorSnapshot] = list()

class QueryRequest():
    pass