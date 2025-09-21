from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.main import get_session
from src.transactions.service import TransactionService

transaction_router = APIRouter()

@transaction_router.post("/upload")
async def upload_transactions():
    pass

@transaction_router.get("/summary/{user_id}")
async def get_transaction_summary(
        user_id: int,
        session: AsyncSession = Depends(get_session),
        time_start: datetime | None = Query(None),
        time_end: datetime | None = Query(None)
):
    if time_end is None:
        time_end = datetime.now()
    if time_start is None:
        time_start = datetime.now() - timedelta(days=365)

    summary = await TransactionService(session).get_user_summary(user_id, time_start, time_end)
    return summary