import pytest

from sqlalchemy.ext.asyncio import AsyncSession

from app.settings import CURRENT_APP_HOST

from app.wallets.routes import get_wallet_data

from app.wallets.schemas import WalletAddressRequest, Wallet


@pytest.mark.asyncio(loop_scope="session")
async def test_get_wallet_with_address(async_db_session: AsyncSession):
    wallet = await get_wallet_data(WalletAddressRequest(address='TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7'), db=async_db_session)

    assert wallet.address == 'TLa2f6VPqDgRE67v1736s7bJ8Ray5wYjU7'
    assert Wallet.model_validate(wallet)
