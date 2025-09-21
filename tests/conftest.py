from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel

from src.config import settings
from src import __init__, app
import pytest_asyncio

from src.db.main import get_session

DB_URL = settings.TEST_POSTGRES_URL

test_engine = create_async_engine(
    url=DB_URL,
    echo=True
)

async def test_get_session() -> AsyncSession:
    async_session = async_sessionmaker(
        bind=test_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        yield session



@pytest_asyncio.fixture(scope="session")
async def test_client():
    import src.db.models
    async with test_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    app.dependency_overrides[get_session] = test_get_session

    with TestClient(app) as client:
        yield client
