from sqlmodel.ext.asyncio.session import AsyncSession


class TransactionService:
    def __init__(self, session:AsyncSession):
        self.session = session

    async def upload_transactions(self):
        return {"status": "ok"}

    async def get_user_summary(self):
        return {"status": "ok"}