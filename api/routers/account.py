from typing import Annotated
from fastapi import APIRouter, Depends, Response, status,File, UploadFile
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator
from typing import Annotated

from .contract.viewdashboardresponse import AccountSnapshot

from .utility import CreateRequest
from ..commands import ViewDashboardCashCommand, WidrawCashCommand, DepositCashCommand, PurchaseSecurityCommand, SellSecurityCommand
from .depositcashrequest import DepositCashRequest
from .widrawcashrequest import WidrawCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from ..containers import ApplicationContainer

router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)

@router.get("/dashboard", tags=["accounts"])
@inject
async def view_dashboard(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])],
    payload : PurchaseSecurityRequest):
 
    command : ViewDashboardCashCommand = ViewDashboardCashCommand()
    command.externalAccountId = "CAS/104948-LI/0"
    entity = await mediator.send_async(command)
       
    response : AccountSnapshot = AccountSnapshot()
    return response

