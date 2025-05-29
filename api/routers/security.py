from typing import Annotated
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator

from .contract.syncunitpricerequest import SyncUnitPriceRequest
from ..commands import SyncLivePriceCommand
from ..containers import ApplicationContainer

securityResourceRouter = APIRouter(
    prefix="/security",
    responses={404: {"description": "Not found"}},
)


@securityResourceRouter.post("/syncprice", tags=["security"])
@inject
async def sync_unitprice(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : SyncUnitPriceRequest):
 
    commands = [SyncLivePriceCommand(securityId=item.symbol, unitPrice=item.price, date= item.lastTradedTime) for item in payload.reqTradeSummery]
    
    for command in commands:
        await mediator.send_async(command)
    
    return "OK"