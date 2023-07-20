from pydantic import BaseModel, ConfigDict, conint
from typing import Optional
from datetime import datetime
from .clientes import Cliente
from .comodatos import ComodatoOut


class ReciboBase(BaseModel):
    monto_recibo: int
    cliente_id: int
    comodato_id: int


class ReciboCreate(ReciboBase):
    pass


class ReciboOut(ReciboBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    fecha_registro: datetime
    cliente: Cliente
    comodato: ComodatoOut

