from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.src.main import app

from functools import lru_cache
from app.utils import config
from app.database.database import get_db
from app.database.database import Base

# pytest
# pytest -v : aclara que códigos pasan
# pytest -v -s: imprime los print por console
# pytest -v -s  module/file.py: elegir 1 test
# pytest --disable-warnings -v: corre todos y te da detalles
# pytest --disable-warnings -v -x: corre hasta el primer FAILED

@lru_cache()
def get_settings():
    return config.Settings()

settings = get_settings()

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture()
def test_cliente(client):
    # definir cliente data
    cliente_data = {
    "dni": 40555888,
    "nombre": "José",
    "apellido": "Espinosa",
    "direccion": "La Rioja 1234",
    "barrio": "La Rioja",
    "localidad": "La RIOJA",
    "telefono": "3516105487",
    "email": "joseespi@mail.com",
    "vehiculo": "VW Suran 2018",
    "patente": "ABC123",
    "fecha_cumple": "10/10/1990"
    }
    
    # enviar request con la data
    response = client.post("/clientes/", json=cliente_data)
    # assertear el status code el response
    assert response.status_code == 201

    # definir el cliente en formato json
    # retornar el cliente
    return response.json()
    


# Fixture de crear usuario
# Fixture de crear token
# Fixture de crear usuario autorizado
# Fixture de usuario autorizado crea clientes



