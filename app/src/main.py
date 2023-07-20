from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated
from sqlalchemy.orm import Session
from ..utils import config
from ..database import models
from ..database.database import engine, get_db
from .schemas.clientes import ClienteOut, ClienteCreate
from .api import clientes, comodatos, recibos


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clientes.router)
app.include_router(comodatos.router)
app.include_router(recibos.router)


@app.get("/")
async def root():
    return {"data": "Hola mundo"}
