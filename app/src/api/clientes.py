from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from ..schemas.clientes import Cliente, ClienteOut, ClienteCreate, ClienteUpdate
from ...database import models
from ...database.database import get_db

router = APIRouter(
    prefix="/clientes",
    tags=['Clientes']
)


# Create

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClienteOut)
async def create_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    cliente_dni = cliente.model_dump()["dni"]

    db_cliente = db.query(models.Cliente).filter(
        models.Cliente.dni == cliente_dni).first()
    if db_cliente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cliente con DNI {cliente_dni} ya existe")

    cliente_nuevo = models.Cliente(**cliente.model_dump())
    db.add(cliente_nuevo)
    db.commit()
    db.refresh(cliente_nuevo)

    cliente_nuevo.fecha_cumple = cliente_nuevo.fecha_cumple.strftime(
        "%d/%m/%Y")
    return cliente_nuevo


# Read all

@router.get("/", response_model=List[Cliente])
async def get_clientes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    clientes = db.query(models.Cliente).offset(skip).limit(limit).all()
    return clientes


# Read one -

@router.get("/{cliente_id}", response_model=ClienteOut)
async def read_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id).first()
    if not db_cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    db_cliente.fecha_cumple = db_cliente.fecha_cumple.strftime("%d/%m/%Y")
    return db_cliente


# Read one - by DNI

@router.get("/dni/", response_model=ClienteOut)
async def read_cliente_by_dni(cliente_dni: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(
        models.Cliente.dni == cliente_dni).first()
    if not db_cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    db_cliente.fecha_cumple = db_cliente.fecha_cumple.strftime("%d/%m/%Y")
    return db_cliente


# Update

@router.put("/{cliente_id}", response_model=ClienteOut)
async def update_cliente(cliente_id: int, cliente_actualizado: ClienteUpdate, db: Session = Depends(get_db)):
    cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cliente {cliente_id} no encontrado")

    for field, value in cliente_actualizado.model_dump(exclude_unset=True).items():
        setattr(cliente, field, value)

    db.commit()
    db.refresh(cliente)
    cliente.fecha_cumple = cliente.fecha_cumple.strftime("%d/%m/%Y")

    return cliente


# Delete

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cliente(cliente_id: int, db: Session = Depends(get_db)):
    db_cliente = db.query(models.Cliente).filter(
        models.Cliente.id == cliente_id)
    if not db_cliente.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    db_cliente.delete(synchronize_session=False)
    db.commit()
    return None
