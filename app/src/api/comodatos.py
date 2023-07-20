from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from ...database import models
from ...database.database import get_db
from ..schemas.comodatos import ComodatoOut, ComodatoCreate, ComodatoUpdate

router = APIRouter(
    prefix="/comodatos",
    tags=['Comodatos']
)


# Create

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ComodatoOut)
async def create_comodato(comodato: ComodatoCreate, db: Session = Depends(get_db)):
    comodato_nuevo = models.Comodato(**comodato.model_dump())

    db.add(comodato_nuevo)
    db.commit()
    db.refresh(comodato_nuevo)

    return comodato_nuevo


# Read all

@router.get("/", response_model=List[ComodatoOut])
async def get_comodatos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    comodatos = db.query(models.Comodato).offset(skip).limit(limit).all()
    return comodatos


# Read one

@router.get("/{comodato_id}", response_model=ComodatoOut)
async def read_comodato(comodato_id: int, db: Session = Depends(get_db)):
    db_comodato = db.query(models.Comodato).filter(
        models.Comodato.id == comodato_id).first()
    if not db_comodato:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comodato not found")
    return db_comodato


# Update

@router.put("/{comodato_id}", response_model=ComodatoOut)
async def update_comodato(comodato_id: int, comodato_actualizado: ComodatoUpdate, db: Session = Depends(get_db)):
    comodato = db.query(models.Comodato).filter(
        models.Comodato.id == comodato_id).first()

    if not comodato:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comodato {comodato_id} no encontrado")

    for field, value in comodato_actualizado.model_dump(exclude_unset=True).items():
        setattr(comodato, field, value)

    db.commit()
    db.refresh(comodato)

    return comodato


# Delete

@router.delete("/{comodato_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comodato(comodato_id: int, db: Session = Depends(get_db)):
    db_comodato = db.query(models.Comodato).filter(
        models.Comodato.id == comodato_id)
    if not db_comodato.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comodato not found")
    db_comodato.delete(synchronize_session=False)
    db.commit()
    return None
