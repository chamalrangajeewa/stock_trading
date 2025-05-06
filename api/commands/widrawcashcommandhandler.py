from datetime import datetime
from pydantic import BaseModel

from api.persistence.service import databaseService

class WidrawCashCommand:
   externalId : str
   accountId : str
   date : datetime
   amount : float

class WidrawCashCommandHandler():

    def __init__(self, databaseService : databaseService):
       self._databaseService = databaseService       

    async def handle(self, request: WidrawCashCommand) -> str:
       return await self._databaseService.process()