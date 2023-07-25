from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base


class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, nullable=False)
    dni = Column(Integer, nullable=False, unique=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    barrio = Column(String, nullable=False)
    localidad = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)
    vehiculo = Column(String, nullable=False)
    patente = Column(String(8), nullable=False)
    fecha_cumple = Column(Date, nullable=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))

    comodatos = relationship("Comodato", back_populates="cliente")
    recibos = relationship("Recibo", back_populates="cliente")


class Comodato(Base):
    __tablename__ = "comodatos"
    id = Column(Integer, primary_key=True, nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))
    fecha_devolucion = Column(Date, nullable=True, server_default=None)
    devuelto = Column(Boolean, nullable=False, default=False)
    barril_7_8_9_litros = Column(Integer, nullable=False, default=0)
    barril_10_12_litros = Column(Integer, nullable=False, default=0)
    barril_18_litros = Column(Integer, nullable=False, default=0)
    barril_25_litros = Column(Integer, nullable=False, default=0)
    barril_30_litros = Column(Integer, nullable=False, default=0)
    barril_40_50_litros = Column(Integer, nullable=False, default=0)
    choppera_sin_barril = Column(Integer, nullable=False, default=0)
    reductor_presion = Column(Integer, nullable=False, default=0)
    tubo_CO2 = Column(Integer, nullable=False, default=0)
    peso_tubo_CO2 = Column(Integer, nullable=False, default=0)
    valvula_automatica = Column(Integer, nullable=False, default=0)
    cabezal_10_litros = Column(Integer, nullable=False, default=0)
    adicionales = Column(String, nullable=True)
    observaciones = Column(String, nullable=True)

    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="comodatos")
    recibos = relationship("Recibo", back_populates="comodato")


class Recibo(Base):
    __tablename__ = "recibos"
    id = Column(Integer, primary_key=True, nullable=False)
    monto_recibo = Column(Integer, nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))
    cliente_id = Column(Integer, ForeignKey(
        "clientes.id", ondelete="CASCADE"), nullable=False)
    cliente = relationship("Cliente")
    comodato_id = Column(Integer, ForeignKey(
        "comodatos.id", ondelete="CASCADE"), nullable=False)
    comodato = relationship("Comodato")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
