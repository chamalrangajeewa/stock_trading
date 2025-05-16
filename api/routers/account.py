from typing import Annotated
from fastapi import APIRouter, Depends, Response, status,File, UploadFile
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator
from typing import Annotated
import pandas as pd
from io import BytesIO

from .contract.viewdashboardresponse import AccountSnapshot

from .utility import CreateRequest
from ..commands import WidrawCashCommand, DepositCashCommand, PurchaseSecurityCommand, SellSecurityCommand
from .depositcashrequest import DepositCashRequest
from .widrawcashrequest import WidrawCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from ..containers import ApplicationContainer

router = APIRouter(
    prefix="/account",
    responses={404: {"description": "Not found"}},
)

@router.post("/changeallocation", tags=["accounts"])
@inject
async def change_allocation(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : DepositCashRequest):
    
    command : DepositCashCommand = DepositCashCommand()
    command.externalAccountId = payload.accountId
    command.externalId = payload.externalTransactionId
    command.date = payload.transactionDate
    command.netAmount = payload.netAmount
    command.description = payload.description
    command.newBalance = payload.newBalance
    command.settlementDate = payload.settlementDate

    return await mediator.send_async(command)
 

@router.get("/dashboard", tags=["accounts"])
@inject
async def view_dashboard(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])],
    payload : PurchaseSecurityRequest):
 
    command : PurchaseSecurityCommand = PurchaseSecurityCommand()
    entity = await mediator.send_async(command)

       
    response : AccountSnapshot = AccountSnapshot()
    return response;

