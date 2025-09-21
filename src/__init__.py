from contextlib import asynccontextmanager

from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting up.")
    yield
    print("server is shutting down.")

app = FastAPI(
    title="Transaction Service",
    description="A simple web service for a transaction application.",
    version="0.0.1",
    lifespan=lifespan
)