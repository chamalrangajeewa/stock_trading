from typing import Annotated, ReadOnly
from fastapi import APIRouter, Depends, Query
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator

from .contract.adjustAllocationAmountRequest import AdjustAllocationAmountRequest
from .contract.adjustSectorAllocationPercentageRequest import AdjustSectorAllocationPercentageRequest
from .contract.adjustSecurityAllocationPercentageRequest import AdjustSecurityAllocationPercentageRequest
from .contract.stocksplitRequest import StocksplitRequest

from ..commands import ViewDashboardCashCommand, AdjustAccountAllocationAmountCommand, AdjustSectorAllocationPercentageCommand, AdjustSecurityAllocationPercentageCommand, StocksplitCommand
from ..containers import ApplicationContainer

TAG = "portfolio"

router = APIRouter(
    prefix="/portfolio",
    responses={404: {"description": "Not found"}},
)

@router.get("/view", tags=[TAG])
@inject
async def view_portfolio(
    accountId: Annotated[str, Query(title="External Account Id", description="This is the Id allocated from the broker.")],
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):

    command : ViewDashboardCashCommand = ViewDashboardCashCommand()
    command.externalAccountId = accountId
    entity = await mediator.send_async(command)

    return entity


@router.put("/adjust-allocation-amount", tags=[TAG])
@inject
async def adjust_portfolio_allocation_amount(
    payload : AdjustAllocationAmountRequest,
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : AdjustAccountAllocationAmountCommand = AdjustAccountAllocationAmountCommand(
        externalAccountId=payload.accountId, 
        allocationAmount = payload.allocationAmount)
    
    await mediator.send_async(command)


@router.put("/sector/adjust-allocation-percentage", tags=[TAG])
@inject
async def adjust_sector_allocation_percentage(
    payload : AdjustSectorAllocationPercentageRequest,
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : AdjustSectorAllocationPercentageCommand = AdjustSectorAllocationPercentageCommand(
        externalAccountId = payload.accountId, 
        sectorName = payload.name,
        allocationPercentage = payload.allocationPercentage)
    
    await mediator.send_async(command)


@router.put("/security/adjust-allocation-percentage", tags=[TAG])
@inject
async def adjust_security_allocation_percentage(
    payload : AdjustSecurityAllocationPercentageRequest,
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : AdjustSecurityAllocationPercentageCommand = AdjustSecurityAllocationPercentageCommand(
        externalAccountId = payload.accountId, 
        securityId = payload.securityId,
        allocationPercentage = payload.allocationPercentage)
    
    await mediator.send_async(command)


@router.put("/security/stocksplit", tags=[TAG])
@inject
async def stocksplit(
    payload : StocksplitRequest,
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : StocksplitCommand = StocksplitCommand(
        externalAccountId = payload.accountId, 
        securityId = payload.securityId,
        quantity = payload.quantity)
    
    await mediator.send_async(command)