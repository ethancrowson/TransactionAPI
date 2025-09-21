from datetime import datetime
from decimal import Decimal
from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4

class Transaction(SQLModel, table=True):
    __tablename__ = 'transactions'

    transaction_id:UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            default=uuid4
        )
    )
    user_id:int
    product_id:int
    timestamp:datetime
    transaction_amount:Decimal

    def __repr__(self) -> str:
        return f"<Transaction => {self.transaction_id}"