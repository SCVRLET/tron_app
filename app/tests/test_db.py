import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from datetime import datetime

from app.wallets.crud import create_wallet_request

from app.wallets.schemas import Wallet


@pytest.mark.asyncio(loop_scope="session")
async def test_create_wallet_in_db(async_db_session: AsyncSession):
    wallet_for_creation_data = dict(address="TRjE1H8dxypKM1NZRdysbs9wo7huR4bdNz",
        balance=100,
        energy=500,
        bandwidth=3000,
    )

    created_wallet = await create_wallet_request(async_db_session, **wallet_for_creation_data)

    assert wallet_for_creation_data == Wallet.model_validate(created_wallet).model_dump(exclude="created_at")
