from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, Response, status,File, UploadFile
from pydantic import BaseModel
from dependency_injector.wiring import Provide, inject
from api.commands.depositcashcommandhandler import DepositCashCommand
from ..containers import ApplicationContainer
from api.routers.service import Service
from api.routers.containers import RouteContainer
from mediatr import Mediator

class DepositCashRequest(BaseModel):
    accountId : str
    amount : float
    externalTransactionId : str
    transactionDate: datetime    
    
router = APIRouter(
    prefix="/transactions",
    responses={404: {"description": "Not found"}},
)

@router.post("/cashIn", tags=["transactions"])
@inject
async def deposit_cash(
    mediator: Annotated[Mediator, Depends(Provide[ApplicationContainer.mediator])], 
    payload : DepositCashRequest):
    return await mediator.send_async(DepositCashCommand())
 
# @router.get("/", tags=["transactions"])
# @inject
# async def get_transactions():
#     return {"username": "all transactions"}

# @router.get("/{trx_id}", tags=["transactions"])
# async def get_transaction(trx_id : str):
#     return {"username": trx_id}

# @router.post("/purchase", tags=["transactions"])
# async def buy_security():
#     return {"username": "fakecurrentuser"}

# @router.post("/sale", tags=["transactions"])
# async def sell_security():
#     return {"username": "fakecurrentuser"}


# @router.post("/cashOut", tags=["transactions"])
# async def widraw_cash():
#     return {"username": "fakecurrentuser"}

# @router.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}