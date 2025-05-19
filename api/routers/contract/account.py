from typing import Annotated
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator

from .contract.syncunitpricerequest import SyncUnitPriceRequest
from ..commands import ViewDashboardCashCommand, SyncLivePriceCommand
from ..containers import ApplicationContainer

router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)


@router.post("/syncprice", tags=["security"])
@inject
async def sync_unitprice(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : SyncUnitPriceRequest):
 
    commands = [SyncLivePriceCommand(securityId=item.symbol, unitPrice=item.price, date= item.lastTradedTime) for item in payload.reqTradeSummery]
    
    for command in commands:
        # print(command)
        await mediator.send_async(command)
    
    return "OK"

@router.get("/dashboard", tags=["accounts"])
@inject
async def view_dashboard(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : ViewDashboardCashCommand = ViewDashboardCashCommand()
    command.externalAccountId = str("CAS/104948-LI/0")
    entity = await mediator.send_async(command)

    return entity