from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import settings

async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)

async def init_db():
    async with AsyncSession(async_engine) as session:

        statement = text("SELECT 'hello';")

        result = await session.exec(statement)

        print(result)
