from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.wallets.tron_api import get_wallet_info

from app.wallets.crud import create_wallet_request, get_wallet_requests

from app.wallets.schemas import Wallet, WalletAddressRequest, RequestedWalletsList

from app.db_helper import get_db


router = APIRouter()

@router.post("/wallet/", response_model=Wallet)
async def get_wallet_data(request: WalletAddressRequest, db: AsyncSession = Depends(get_db)):
    data = await get_wallet_info(request.address)
    if data is None:
        raise HTTPException(status_code=404, detail="Wallet not found")

    wallet_entry = await create_wallet_request(db, request.address, **data)

    return Wallet.model_validate(wallet_entry)


@router.get("/wallets/", response_model=RequestedWalletsList)
async def list_wallet_requests(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    wallets = await get_wallet_requests(db, skip, limit)

    return RequestedWalletsList(requested_wallets=[Wallet.model_validate(wallet) for wallet in wallets])

