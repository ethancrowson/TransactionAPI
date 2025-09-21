from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings

async_engine = create_async_engine(
    url=settings.POSTGRES_URL,
    echo=True
)