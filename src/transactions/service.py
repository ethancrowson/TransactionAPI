from datetime import datetime

from fastapi import UploadFile
from sqlalchemy import func, select, and_
from sqlmodel.ext.asyncio.session import AsyncSession

from src.db.models import Transaction


class TransactionService:
    def __init__(self, session:AsyncSession):
        # Store the database session for making queries.
        self.session = session

    async def upload_transactions(self, file: UploadFile):
        return {"status": "ok"}

    # Get a summary of transactions for a given user between two dates
    async def get_user_summary(self,user_id:int,time_start:datetime,time_end:datetime):
        statement = select(
            func.count().label("count"),
            func.min(Transaction.transaction_amount).label("min"),
            func.max(Transaction.transaction_amount).label("max"),
            func.avg(Transaction.transaction_amount).label("mean"),
        ).where(and_(Transaction.user_id == user_id, Transaction.timestamp >= time_start,
                     Transaction.timestamp <= time_end))

        result = await self.session.exec(statement)
        row = result.one()

        # Return a structured JSON response
        return {
            "user_id": user_id,
            "start": time_start,
            "end": time_end,
            "count": row.count,
            "min": float(row.min) if row.min is not None else None,
            "max": float(row.max) if row.max is not None else None,
            "mean": float(row.mean) if row.mean is not None else None,
        }