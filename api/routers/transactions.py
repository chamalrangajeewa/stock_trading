from typing import Annotated
from fastapi import APIRouter, Depends, Response, status,File, UploadFile
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator
import pandas as pd
from io import BytesIO

from .utility import CreateRequest
from ..commands import WidrawCashCommand, DepositCashCommand, PurchaseSecurityCommand, SellSecurityCommand
from .depositcashrequest import DepositCashRequest
from .widrawcashrequest import WidrawCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from ..containers import ApplicationContainer

TAG = "transaction"

router = APIRouter(
    prefix="/transaction",
    responses={404: {"description": "Not found"}},
)

@router.post("/cashIn", tags=[TAG])
@inject
async def cash_in(
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
 

@router.post("/purchase", tags=[TAG])
@inject
async def buy_security(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])],
    payload : PurchaseSecurityRequest):
 
    command : PurchaseSecurityCommand = PurchaseSecurityCommand()
    command.externalAccountId = payload.accountId
    command.externalId = payload.externalTransactionId
    command.date = payload.transactionDate
    command.netAmount = payload.netAmount
    command.description = payload.description
    command.newBalance = payload.newBalance
    command.settlementDate = payload.settlementDate

    command.securityId = payload.securityId
    command.unitPrice = payload.unitPrice
    command.fees = payload.fees
    command.quantity = payload.quantity

    return await mediator.send_async(command)
 

@router.post("/sale", tags=[TAG])
@inject
async def sell_security(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : SellSecurityRequest):

    command : SellSecurityCommand = SellSecurityCommand()
    command.externalAccountId = payload.accountId
    command.externalId = payload.externalTransactionId
    command.date = payload.transactionDate
    command.netAmount = payload.netAmount
    command.description = payload.description
    command.newBalance = payload.newBalance
    command.settlementDate = payload.settlementDate

    command.securityId = payload.securityId
    command.unitPrice = payload.unitPrice
    command.fees = payload.fees
    command.quantity = payload.quantity

    return await mediator.send_async(command)


@router.post("/cashout", tags=[TAG])
@inject
async def cash_out(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : WidrawCashRequest):
 
    command : WidrawCashCommand = WidrawCashCommand()
    command.externalAccountId = payload.accountId
    command.externalId = payload.externalTransactionId
    command.date = payload.transactionDate
    command.netAmount = payload.netAmount
    command.description = payload.description
    command.newBalance = payload.newBalance
    command.settlementDate = payload.settlementDate

    return await mediator.send_async(command)
 

@router.post("/bulkimport/", tags=[TAG])
@inject
async def bulk_import(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    file: Annotated[bytes, File()]):
    
    df = pd.read_csv(BytesIO(file))
    commands = [CreateRequest(
            row.Type, 
            row.Account, 
            row.Amount,
            row.Number,
            row.Date,
            row.Particular,
            row.Balance,
            row.SettlementDate,
            row.Security,
            row.Quantity,
            row.Price,
            row.Fees) for row in df.itertuples()]
    
    for command in commands:
        await mediator.send_async(command)

    return "OK"