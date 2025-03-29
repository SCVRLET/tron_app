from tronpy import AsyncTron

from tronpy.exceptions import AddressNotFound


client = AsyncTron(network="nile")

async def get_wallet_info(address: str):
    try:
        account = await client.get_account(address)
        balance = account.get("balance", 0)
        bandwidth = await client.get_bandwidth(address)
        
        resources = await client.get_account_resource(address)
        energy = resources.get("EnergyLimit", 0) 

        return {"balance": balance, "bandwidth": bandwidth, "energy": energy}

    except AddressNotFound:
        return None
