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


def test_read_one_cliente(client, session):

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


def test_read_one_cliente_not_exist(client):
    res = client.get(f"/clientes/88888")
    assert res.status_code == 404


def test_update_cliente(client, session):

    # Create a test cliente
    test_cliente = models.Cliente(
        dni=11122233,
        nombre="Test",
        apellido="Cliente",
        direccion="Test 123",
        barrio="Test",
        localidad="Test",
        telefono="1567867890",
        email="test@test.com",
        vehiculo="Test",
        patente="TEST123",
        fecha_cumple="01/01/2000"
    )
    session.add(test_cliente)
    session.commit()
    session.refresh(test_cliente)

    # Make a request to the update_cliente endpoint
    response = client.put(f"/clientes/{test_cliente.id}", json={
        "dni": 87654321,
        "nombre": "Nuevo",
        "apellido": "Cliente",
        "direccion": "Nuevo 123",
        "barrio": "Nuevo",
        "localidad": "Nuevo",
        "telefono": "0987654321",
        "email": "nuevo@test.com",
        "vehiculo": "Nuevo",
        "patente": "NUE123",
        "fecha_cumple": "02/02/2000"
    })

    # Check that the response status code is 200
    assert response.status_code == 200

    # Check that the response body matches the expected output
    expected_output = {
        "id": test_cliente.id,
        "dni": 87654321,
        "nombre": "Nuevo",
        "apellido": "Cliente",
        "direccion": "Nuevo 123",
        "barrio": "Nuevo",
        "localidad": "Nuevo",
        "telefono": "0987654321",
        "email": "nuevo@test.com",
        "vehiculo": "Nuevo",
        "patente": "NUE123",
        "fecha_cumple": "02/02/2000"
    }
    assert response.json() == expected_output

    # Check that the cliente was updated in the database
    updated_cliente = session.query(models.Cliente).filter(
        models.Cliente.id == test_cliente.id).first()
    assert updated_cliente.dni == expected_output["dni"]
    assert updated_cliente.nombre == expected_output["nombre"]
    assert updated_cliente.apellido == expected_output["apellido"]
    assert updated_cliente.direccion == expected_output["direccion"]
    assert updated_cliente.barrio == expected_output["barrio"]
    assert updated_cliente.localidad == expected_output["localidad"]
    assert updated_cliente.telefono == expected_output["telefono"]
    assert updated_cliente.email == expected_output["email"]
    assert updated_cliente.vehiculo == expected_output["vehiculo"]
    assert updated_cliente.patente == expected_output["patente"]
    assert updated_cliente.fecha_cumple.strftime(
        "%d/%m/%Y") == expected_output["fecha_cumple"]

    # Check that the response body matches the ClienteOut schema
    response_schema = clientes.ClienteOut(**response.json())
    assert response_schema.id == test_cliente.id
    assert response_schema.dni == expected_output["dni"]
    assert response_schema.nombre == expected_output["nombre"]
    assert response_schema.apellido == expected_output["apellido"]
    assert response_schema.direccion == expected_output["direccion"]
    assert response_schema.barrio == expected_output["barrio"]
    assert response_schema.localidad == expected_output["localidad"]
    assert response_schema.telefono == expected_output["telefono"]
    assert response_schema.email == expected_output["email"]
    assert response_schema.vehiculo == expected_output["vehiculo"]
    assert response_schema.patente == expected_output["patente"]
    assert response_schema.fecha_cumple == expected_output["fecha_cumple"]


def test_update_cliente_not_found(client, session):

    # Make a request to the update_cliente endpoint
    response = client.put("/clientes/100000", json={
        "dni": 87654321,
        "nombre": "Nuevo",
        "apellido": "Cliente",
        "direccion": "Nuevo 123",
        "barrio": "Nuevo",
        "localidad": "Nuevo",
        "telefono": "0987654321",
        "email": "test@test.com",
        "vehiculo": "Nuevo",
        "patente": "NUE123",
        "fecha_cumple": "02/02/2000"
    })

    # Check that the response status code is 404
    assert response.status_code == 404


def test_delete_cliente(client, session):

    # Create a test cliente
    test_cliente = models.Cliente(
        dni=10000000,
        nombre="Test",
        apellido="Cliente",
        direccion="Test 123",
        barrio="Test",
        localidad="Test",
        telefono="8815535545",
        email="test@test.com",
        vehiculo="Test",
        patente="TEST123",
        fecha_cumple="01/01/2000"
    )
    session.add(test_cliente)
    session.commit()
    session.refresh(test_cliente)

    # Make a request to the delete_cliente endpoint
    response = client.delete(f"/clientes/{test_cliente.id}")

    # Check that the response status code is 204
    assert response.status_code == 204
