from fastapi import FastAPI

from .database import create_db_and_tables
from .routers import gifts


app = FastAPI()
app.include_router(gifts.router)
create_db_and_tables()
