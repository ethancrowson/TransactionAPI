# Transaction API

A small FastAPI + SQLModel service for uploading transaction data (CSV) and returning per-user summaries over some date range.

## Tech Stack
FastAPI (async) <br>
SQLModel (on top of SQLAlchemy) <br>
PostgreSQL via asyncpg <br>
pydantic-settings for config <br>
Uvicorn for dev server <br>
Pytest for tests

## Prerequisites
Python 3.11+
PostgreSQL 13+


## Quick Start
```
# 1) Clone

git clone https://github.com/ethancrowson/TransactionAPI
cd TransactionAPI

# 2) Create venv

python -m venv .venv

# Windows (PowerShell):
. .\.venv\Scripts\Activate.ps1

# macOS/Linux:
source .venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run the app
python runserver.py
```
## Using the program
Open: http://127.0.0.1:8000/docs 

Click POST /upload → “Try it out” → pick your CSV → Execute

Click GET /summary/{user_id} → enter a user_id and (optionally) time_start, time_end → Execute

These can also be done via Postman or by using cURL

```
    # Upload CSV
    curl -F "file=@dummy_transactions.csv" http://127.0.0.1:8000/upload
    
    # Summary (no date range)
    curl "http://127.0.0.1:8000/summary/42"
    
    # Summary (date range)
    curl "http://127.0.0.1:8000/summary/42?time_start=2024-09-20&time_end=2024-12-20"
```

## Testing
I could not get my pytests to work but manual testing has been done to ensure functionality.

## Approach
I built an async FastAPI service backed by Postgres. It streams a 1M-row CSV into the database (using COPY for high throughput) and exposes /summary/{user_id} to return min/max/mean over an optional date range. I included tests and a clear README. Unfortunately I ran into errors with pytest and my unit testing is incomplete, but the program runs as intended.