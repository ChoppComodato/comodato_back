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


# @app.get("/clientes/", response_model=List[ClienteOut])
# def get_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
#     return clientes


# @app.post("/clientes/", status_code=status.HTTP_201_CREATED, response_model=ClienteOut)
# async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
#     cliente_nuevo = models.Cliente(**cliente.model_dump())

#     db.add(cliente_nuevo)
#     db.commit()
#     db.refresh(cliente_nuevo)

#     return cliente_nuevo

app.include_router(clientes.router)

@app.get("/")
async def root():
    return {"data": "Hola mundo"}
