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
    telefono = Column(String, nullable=False, unique=True)
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
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    # a partir de las 00:00:00 del día actual
    fecha_comodato = Column(Date, nullable=False)
    # hasta las 23:59:59 del día pasado mañana
    fecha_devolucion = Column(Date, nullable=False)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))
    estado = Column(Boolean, nullable=False, default=True)
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


    cliente = relationship("Cliente", back_populates="comodatos")
    recibos = relationship("Recibo", back_populates="comodato")



class Recibo(Base):
    __tablename__ = "recibos"
    id = Column(Integer, primary_key=True, nullable=False)
    comodato_id = Column(Integer, ForeignKey("comodatos.id"))
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    monto_recibo = Column(Integer, nullable=False)
    estado = Column(Boolean, nullable=False, default=True)
    fecha_registro = Column(TIMESTAMP(timezone=True),
                            nullable=False, server_default=text('now()'))
    cliente = relationship("Cliente", back_populates="recibos")
    comodato = relationship("Comodato", back_populates="recibos")

