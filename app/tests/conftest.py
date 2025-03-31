import asyncio

import pytest

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker
)

from sqlalchemy.exc import ProgrammingError

from sqlalchemy.sql import text

from app.models import Base

from app.settings import TEST_DB_URL


engine: AsyncEngine = create_async_engine(TEST_DB_URL, echo=True)

AsyncTestingSessionLocal = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

admin_engine: AsyncEngine = create_async_engine(
    TEST_DB_URL, isolation_level="AUTOCOMMIT"
)


async def create_test_database():
    async with admin_engine.connect() as connection:
        try:
            db_name = TEST_DB_URL.rsplit("/", 1)[-1]
            await connection.execute(text(f"CREATE DATABASE {db_name}"))
        except ProgrammingError:
            print("Database already exists, continuing...")


@pytest.fixture(scope="session", autouse=True)
async def setup_test_database():
    await create_test_database()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session")
async def async_db_session() -> AsyncSession:
   async with AsyncTestingSessionLocal() as session:
        yield session
        await session.rollback()
