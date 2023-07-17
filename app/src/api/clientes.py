from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from ..schemas.clientes import ClienteOut, ClienteCreate, ClienteUpdate
from ...database import models
from ...database.database import get_db

router = APIRouter(
    prefix="/clientes",
    tags=['Clientes']
)

@router.get("/", response_model=List[ClienteOut])
def get_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    return clientes


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClienteOut)
async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    cliente_nuevo = models.Cliente(**cliente.model_dump())

    db.add(cliente_nuevo)
    db.commit()
    db.refresh(cliente_nuevo)

    return cliente_nuevo