from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from ...database import models
from ...database.database import get_db
from ..schemas.recibos import ReciboCreate, ReciboOut

router = APIRouter(
    prefix="/recibos",
    tags=['Recibos']
)


#  Create

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ReciboOut)
async def create_recibo(recibo: ReciboCreate, db: Session = Depends(get_db)):
    
    cliente_id = recibo.model_dump()["cliente_id"]
    comodato_id = recibo.model_dump()["comodato_id"]

    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    comodato = db.query(models.Comodato).filter(models.Comodato.id == comodato_id).first()
    
    if not cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Cliente {cliente_id} no encontrado")
    
    if not comodato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comodato {comodato_id} no encontrado")
    

    recibo_nuevo = recibo.model_dump()
    recibo_nuevo["cliente"] = cliente
    recibo_nuevo["comodato"] = comodato

    recibo_nuevo = models.Recibo(**recibo.model_dump())

    
    
    db.add(recibo_nuevo)
    db.commit()
    db.refresh(recibo_nuevo)



    return recibo_nuevo


# Get all

@router.get("/", response_model=List[ReciboOut])
async def get_recibos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    recibos = db.query(models.Recibo).offset(skip).limit(limit).all()
    return recibos


# Read one

@router.get("/{recibo_id}", response_model=ReciboOut)
async def read_recibo(recibo_id: int, db: Session = Depends(get_db)):
    db_recibo = db.query(models.Recibo).filter(
        models.Recibo.id == recibo_id).first()
    if not db_recibo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Recibo not found")
    return db_recibo


# Update

@router.put("/{recibo_id}", response_model=ReciboOut)
async def update_recibo(recibo_id: int, recibo_actualizado: ReciboCreate, db: Session = Depends(get_db)):
    recibo = db.query(models.Recibo).filter(
        models.Recibo.id == recibo_id).first()

    if not recibo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Recibo {recibo_id} no encontrado")

    for field, value in recibo_actualizado.model_dump().items():
        setattr(recibo, field, value)

    db.commit()
    db.refresh(recibo)

    return recibo


# Delete

@router.delete("/{recibo_id}", response_model=ReciboOut)
async def delete_recibo(recibo_id: int, db: Session = Depends(get_db)):
    recibo = db.query(models.Recibo).filter(
        models.Recibo.id == recibo_id).first()

    if not recibo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Recibo {recibo_id} no encontrado")

    db.delete(recibo)
    db.commit()