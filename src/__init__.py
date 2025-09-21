from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.db.main import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting up.")
    await init_db()
    yield
    print("server is shutting down.")

app = FastAPI(
    title="Transaction Service",
    description="A simple web service for a transaction application.",
    version="0.0.1",
    lifespan=lifespan
)