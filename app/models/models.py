from sqlalchemy import Column, String, Integer, DateTime, BigInteger

from sqlalchemy.sql import func

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class RequestedWallet(Base):
    __tablename__ = "requested_wallets"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, nullable=False)
    balance = Column(BigInteger, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now())
