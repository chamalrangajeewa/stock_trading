from api.models.transaction import Transaction
from pydantic import BaseModel
from typing import List

class Security(BaseModel):
    name : str
    externalId : str
    transactions: List[Transaction]