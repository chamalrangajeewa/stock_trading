from datetime import datetime
from pydantic import BaseModel

from api.commands.transactionCommand import TransactionCreateCommand

class TransactionCommandHandler(BaseModel):
    
    def __init__(self):
       pass

    def Handle(payload : TransactionCreateCommand):
       pass