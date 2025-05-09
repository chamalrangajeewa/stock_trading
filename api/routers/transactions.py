from typing import Annotated
from fastapi import APIRouter, Depends, Response, status,File, UploadFile
from dependency_injector.wiring import Provide, inject
from mediatr import Mediator
from typing import Annotated
import pandas as pd
from io import BytesIO

from .utility import CreateRequest
from ..commands import WidrawCashCommand,DepositCashCommand,PurchaseSecurityCommand,SellSecurityCommand
from .depositcashrequest import DepositCashRequest
from .widrawcashrequest import WidrawCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from ..containers import ApplicationContainer

router = APIRouter(
    prefix="/transactions",
    responses={404: {"description": "Not found"}},
)

@router.post("/cashIn", tags=["transactions"])
@inject
async def deposit_cash(
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
 

@router.post("/purchase", tags=["transactions"])
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
 

@router.post("/sale", tags=["transactions"])
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


@router.post("/cashOut", tags=["transactions"])
@inject
async def widraw_cash(
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
 

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@router.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    
    squares = [x**2 for x in range(10)]
    df = pd.read_csv(BytesIO(file))
    for row in df.itertuples():
        x, *y = row       
        _, a, b, c, d, e, f, g, h, i, g, h, i = row
        CreateRequest(
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
            row.Fees)
        print(row)
    return df.to_dict()