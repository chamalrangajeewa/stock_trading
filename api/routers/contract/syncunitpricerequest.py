from datetime import datetime
from typing import List
from pydantic import BaseModel

class UnitPriceInfo(BaseModel):

    symbol : str
    lastTradedTime : datetime
    price : float


class SyncUnitPriceRequest(BaseModel):

    reqTradeSummery: List[UnitPriceInfo] = list()