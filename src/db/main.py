from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import settings

# Create an async engine (connection to the database).
async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)

# Initialise the database (create tables).
async def init_db():
    import src.db.models # import models so metadata includes them.
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

# Dependency to get a new async session for each request.
async def get_session() -> AsyncSession:
    async_session = async_sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False # objects remain usable after commit.
    )

    # Provide a session for the request, and automatically close it after use.
    async with async_session() as session:
        yield session