from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, ARRAY, Date
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base
from typing import List



class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    dni = Column(Integer, primary_key=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    barrio = Column(String, nullable=False)
    localidad = Column(String, nullable=False)
    telefono = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False)
    vehiculo = Column(String, nullable=False)
    patente = Column(String(8), nullable=False)
    
    fecha_cumple = Column(Date, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    