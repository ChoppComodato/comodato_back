from functools import lru_cache

from fastapi import Depends, FastAPI
from typing_extensions import Annotated

from ..utils import config

app = FastAPI()


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/info")
async def info(settings: Annotated[config.Settings, Depends(get_settings)]):
    return {
        "database_name": settings.database_name,
        "database_username": settings.database_username,
    }

@app.get("/")
async def root():
    return {"data": "Hola mundo"}
