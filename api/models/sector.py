from api.models.security import Security
from pydantic import BaseModel
from typing import List

from api.models.securitysnapshot import SecuritySnapshot

class Sector(BaseModel):
    name : str
    externalId : str
    securities: List[Security]

class SectorSnapshot(BaseModel):
    name : str
    externalId : str
    percentageAllocation : float
    realisedAllocation : float   
    securitySnapshots: List[SecuritySnapshot]