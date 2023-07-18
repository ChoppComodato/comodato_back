from typing import List
from fastapi import Depends, FastAPI, HTTPException, status

from typing_extensions import Annotated
from sqlalchemy.orm import Session
from ..utils import config
from ..database import models
from ..database.database import engine, get_db
from .schemas.clientes import ClienteOut, ClienteCreate
from .api import clientes


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(clientes.router)

@app.get("/")
async def root():
    return {"data": "Hola mundo"}
