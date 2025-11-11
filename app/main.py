from fastapi import FastAPI
from app.db import config
from app.models.entities import User
from app.routers import all_routers

app = FastAPI()

for router in all_routers:
    app.include_router(router)
