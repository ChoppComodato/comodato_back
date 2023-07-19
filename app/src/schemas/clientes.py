from pydantic import BaseModel, ConfigDict, EmailStr, conint, constr
from typing import Optional
from datetime import datetime


regex_telefono = r'^(\+?\d{0,3}-?)?\d{0,5}-?\d{0,10}$' # Ej: +54-351-5847755 | 3515847755 | 351-5847755
regex_patente = r'^[a-zA-Z0-9]{6,8}$' # Ej: AA123BB | ABC123

class ClienteCreate(BaseModel):
    dni: conint(gt=1000000, le=99999999)
    nombre: str
    apellido: str
    direccion: str
    barrio: str
    localidad: str
    telefono: constr(pattern=regex_telefono)
    email: EmailStr
    vehiculo: str
    patente: constr(pattern=regex_patente)
    fecha_cumple: Optional[str] = None


class ClienteUpdate(BaseModel):
    dni: Optional[conint(gt=1000000, le=99999999)]
    nombre: Optional[str]
    apellido: Optional[str]
    direccion: Optional[str]
    barrio: Optional[str]
    localidad: Optional[str]
    telefono: Optional[constr(pattern=regex_telefono)]
    email: Optional[EmailStr]
    vehiculo: Optional[str]
    patente: Optional[constr(pattern=regex_patente)]
    fecha_cumple: Optional[str]


class Cliente(BaseModel):
    "Modelo de response para tipo de datos replicados de la base de datos"
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


class ClienteOut(BaseModel):
    "Modelo de response para tipo de datos formato para la interface"
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
    fecha_cumple: str
