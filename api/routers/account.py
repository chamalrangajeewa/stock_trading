from typing import Annotated
from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator
from typing import Annotated

from ..commands import ViewDashboardCashCommand
from .purchasesecurityrequest import PurchaseSecurityRequest
from ..containers import ApplicationContainer

router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)

@router.get("/dashboard", tags=["accounts"])
@inject
async def view_dashboard(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])]):
 
    command : ViewDashboardCashCommand = ViewDashboardCashCommand()
    command.externalAccountId = str("CAS/104948-LI/0")
    entity = await mediator.send_async(command)

    return entity