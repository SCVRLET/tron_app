from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select

from app.models import RequestedWallet


async def create_wallet_request(db: AsyncSession, address: str, balance: int, bandwidth: int, energy: int):
    wallet_entry = RequestedWallet(address=address, balance=balance, bandwidth=bandwidth, energy=energy)
    db.add(wallet_entry)
    await db.commit()
    await db.refresh(wallet_entry)

    return wallet_entry


async def get_wallet_requests(db: AsyncSession, skip: int = 0, limit: int = 10):
    query = select(RequestedWallet).offset(skip).limit(limit).order_by(RequestedWallet.created_at.desc())
    result = await db.execute(query)

    return result.scalars().all()
