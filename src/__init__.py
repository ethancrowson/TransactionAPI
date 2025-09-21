from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db.main import init_db
from src.transactions.routes import transaction_router

# Lifespan context manager: runs code when the app starts up and shuts down.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting up.")
    await init_db() # Initialise database tables at startup.
    yield # App runs here.
    print("server is shutting down.")

# Create the FastAPI app instance.
app = FastAPI(
    title="Transaction Service",
    description="A simple web service for a transaction application.",
    version="0.0.1",
    lifespan=lifespan
)

# Register the transaction router under the app.
app.include_router(transaction_router, tags=["transaction"])