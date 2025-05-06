from datetime import datetime
from dependency_injector import containers, providers
from api.persistence.service import databaseService

class DepositCashCommand:
   externalId : str
   accountId : str
   date : datetime
   amount : float

class DepositCashCommandHandler():
    
   def __init__(self, databaseService : databaseService):
       self._databaseService = databaseService       

   async def handle(self, request: DepositCashCommand) -> str:
       return await self._databaseService.process()


