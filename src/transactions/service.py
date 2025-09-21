from sqlmodel.ext.asyncio.session import AsyncSession


class TransactionService:
    def __init__(self, session:AsyncSession):
        self.session = session