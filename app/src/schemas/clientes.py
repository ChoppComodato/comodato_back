from pydantic import BaseModel, ConfigDict, EmailStr, conint, constr
from typing import Optional
from datetime import datetime


class ClienteCreate(BaseModel):
    dni: conint(gt=1000000, le=99999999)
    nombre: str
    apellido: str
    direccion: str
    barrio: str
    localidad: str
    telefono: constr(pattern=r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$')
    email: EmailStr
    vehiculo: str
    patente: constr(pattern=r'^[a-zA-Z]{3}\d{3}$')
    fecha_cumple: Optional[str] = None


class ClienteUpdate(BaseModel):
    dni: Optional[conint(gt=1000000, le=99999999)]
    nombre: Optional[str]
    apellido: Optional[str]
    direccion: Optional[str]
    barrio: Optional[str]
    localidad: Optional[str]
    telefono: Optional[constr(pattern=(r'^\+?\d{0,3}\d{0,5}-?\d{0,10}$'))]
    email: Optional[EmailStr]
    vehiculo: Optional[str]
    patente: Optional[constr(pattern=(r'^[a-zA-Z]{3}\d{3}$'))]
    fecha_cumple: Optional[str]


class ClienteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    dni: int
    nombre: str
    apellido: str
    direccion: str
    barrio: str
    localidad: str
    telefono: str
    email: str
    vehiculo: str
    patente: str
    fecha_cumple: datetime
    fecha_registro: datetime
