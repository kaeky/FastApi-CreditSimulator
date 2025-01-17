from fastapi import FastAPI

from src.config.router import register_routers

app = FastAPI()

app.include_router(register_routers())