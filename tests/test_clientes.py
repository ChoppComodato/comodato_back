import pytest
from .database import client, session
from app.src.schemas import clientes
from app.database import models


def test_get_all_clientes(client):
    "Test del schema ClienteOut"
    res = client.get("/clientes/")

    def validate(raw_cliente):
        return clientes.ClienteOut(**raw_cliente)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert res.status_code == 200


def test_post_cliente(client):
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
    
    response = client.post("/clientes/", json=cliente_data)
    assert response.status_code == 201

def test_read_cliente(client, session):


    # Create a test cliente
    test_cliente = models.Cliente(
        dni=12345678,
        nombre="Test",
        apellido="Cliente",
        direccion="Test 123",
        barrio="Test",
        localidad="Test",
        telefono="1234567890",
        email="test@test.com",
        vehiculo="Test",
        patente="TEST123",
        fecha_cumple="01/01/2000"
    )
    session.add(test_cliente)
    session.commit()
    session.refresh(test_cliente)

    # Make a request to the read_cliente endpoint
    response = client.get(f"/clientes/{test_cliente.id}")

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response body matches the expected output
    assert response.json() == {
        "id": test_cliente.id,
        "dni": test_cliente.dni,
        "nombre": test_cliente.nombre,
        "apellido": test_cliente.apellido,
        "direccion": test_cliente.direccion,
        "barrio": test_cliente.barrio,
        "localidad": test_cliente.localidad,
        "telefono": test_cliente.telefono,
        "email": test_cliente.email,
        "vehiculo": test_cliente.vehiculo,
        "patente": test_cliente.patente,
        "fecha_cumple": test_cliente.fecha_cumple
    }


# def test_get_one_premio_not_exist(client):
#     res = client.get(f"/v1/premios/88888")
#     assert res.status_code == 404
