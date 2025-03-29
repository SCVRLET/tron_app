import asyncio

import uvicorn

from fastapi import FastAPI

from app.models import Base 

from .db_helper import engine

from .wallets.routes import router as wallets_router


app = FastAPI(title="Tron wallet service")

app.include_router(wallets_router)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await create_tables()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

