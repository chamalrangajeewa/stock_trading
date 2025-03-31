from fastapi import APIRouter
from typing import Annotated

from fastapi import File, UploadFile

router = APIRouter(
    prefix="/transactions",
    responses={404: {"description": "Not found"}},
)

@router.get("/", tags=["transactions"])
async def get_transactions():
    return {"username": "all transactions"}

@router.get("/{trx_id}", tags=["transactions"])
async def get_transaction(trx_id : str):
    return {"username": trx_id}

@router.post("/purchase", tags=["transactions"])
async def buy_security():
    return {"username": "fakecurrentuser"}

@router.post("/sale", tags=["transactions"])
async def sell_security():
    return {"username": "fakecurrentuser"}

@router.post("/cashIn", tags=["transactions"])
async def deposit_cash():
    return {"username": "fakecurrentuser"}

@router.post("/cashOut", tags=["transactions"])
async def widraw_cash():
    return {"username": "fakecurrentuser"}

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}