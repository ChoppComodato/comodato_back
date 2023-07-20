from pydantic import BaseModel, ConfigDict, conint
from typing import Optional
from datetime import datetime

positivos = conint(ge=0)
# Caso: todos los valores deben ser mayores o iguales a cero


class ComodatoCreate(BaseModel):
    # cliente_id: int
    barril_7_8_9_litros: Optional[positivos] = None
    barril_10_12_litros: Optional[positivos] = None
    barril_18_litros: Optional[positivos] = None
    barril_25_litros: Optional[positivos] = None
    barril_30_litros: Optional[positivos] = None
    barril_40_50_litros: Optional[positivos] = None
    choppera_sin_barril: Optional[positivos] = None
    reductor_presion: Optional[positivos] = None
    tubo_CO2: Optional[positivos] = None
    peso_tubo_CO2: Optional[positivos] = None
    valvula_automatica: Optional[positivos] = None
    cabezal_10_litros: Optional[positivos] = None
    adicionales: Optional[str] = None
    observaciones: Optional[str] = None


class ComodatoUpdate(BaseModel):
    fecha_devolucion: Optional[datetime] = datetime.now()
    devuelto: Optional[bool] = True
    barril_7_8_9_litros: Optional[positivos] = None
    barril_10_12_litros: Optional[positivos] = None
    barril_18_litros: Optional[positivos] = None
    barril_25_litros: Optional[positivos] = None
    barril_30_litros: Optional[positivos] = None
    barril_40_50_litros: Optional[positivos] = None
    choppera_sin_barril: Optional[positivos] = None
    reductor_presion: Optional[positivos] = None
    tubo_CO2: Optional[positivos] = None
    peso_tubo_CO2: Optional[positivos] = None
    valvula_automatica: Optional[positivos] = None
    cabezal_10_litros: Optional[positivos] = None
    adicionales: Optional[str] = None
    observaciones: Optional[str] = None


class ComodatoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fecha_registro: datetime
    fecha_devolucion: Optional[datetime] = None
    devuelto: bool
    barril_7_8_9_litros: Optional[positivos] = None
    barril_10_12_litros: Optional[positivos] = None
    barril_18_litros: Optional[positivos] = None
    barril_25_litros: Optional[positivos] = None
    barril_30_litros: Optional[positivos] = None
    barril_40_50_litros: Optional[positivos] = None
    choppera_sin_barril: Optional[positivos] = None
    reductor_presion: Optional[positivos] = None
    tubo_CO2: Optional[positivos] = None
    peso_tubo_CO2: Optional[positivos] = None
    valvula_automatica: Optional[positivos] = None
    cabezal_10_litros: Optional[positivos] = None
    adicionales: Optional[str] = None
    observaciones: Optional[str] = None
