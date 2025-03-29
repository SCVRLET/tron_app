from pydantic import BaseModel, ConfigDict, field_validator

from datetime import datetime

from tronpy.keys import is_base58check_address

from typing import List


class Wallet(BaseModel):
    address: str
    balance: int
    bandwidth: int
    energy: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RequestedWalletsList(BaseModel):
    requested_wallets: List[Wallet]


class WalletAddressRequest(BaseModel):
    address: str

    @field_validator("address")
    def check_address(cls, value):
        if is_base58check_address(value):
            return value

        raise ValueError("Invalid address")
