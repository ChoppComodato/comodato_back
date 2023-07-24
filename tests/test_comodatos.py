from app.src.schemas import comodatos
from app.database import models
import json


def test_create_comodato(client, body_comodato, test_cliente):

    # Create a ComodatoCreate request body
    request_body = body_comodato
    request_body["cliente_id"] = test_cliente.get("id")
    # Send a POST request to the /comodatos path with the request body
    response = client.post("/comodatos", json=request_body)
    # Check the response status code and content
    assert response.status_code == 201


def test_create_comodato_invalid(client, body_comodato_wrong, test_cliente):
    # Create a ComodatoCreate request body
    request_body = body_comodato_wrong
    request_body["cliente_id"] = test_cliente.get("id")
    # Send a POST request to the /comodatos path with the request body
    response = client.post("/comodatos", json=request_body)
    # Check the response status code and content
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "greater_than_equal",
                "loc": ["body", "barril_7_8_9_litros"],
                "msg": "Input should be greater than or equal to 0",
                "input": -1,
                "ctx": {"ge": 0},
                "url": "https://errors.pydantic.dev/2.0.3/v/greater_than_equal"
            }
        ]
    }


def test_read_all_comodatos(client):
    "Test del schema ComodatoOut con el endpoint /Comodatos/ "
    res = client.get("/comodatos/")

    def validate(row):
        return comodatos.ComodatoOut(**row)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert res.status_code == 200


def test_get_one_comodato(client, session, body_comodato, test_cliente):
    # Create a new comodato in the database
    body_comodato["cliente_id"] = test_cliente.get("id")
    test_comodato = models.Comodato(**body_comodato)

    session.add(test_comodato)
    session.commit()
    session.refresh(test_comodato)

    response = client.get(f"/comodatos/{test_comodato.id}")

    assert response.status_code == 200

    # expected = comodatos.ComodatoOut(**test_comodato.__dict__)
    # assert response.json() == expected.model_dump()


def test_update_comodato(client, session, test_cliente):
    #  1) creamos un registro de comodato y lo actualizamos
    test_comodato = models.Comodato(
        cliente_id=test_cliente.get("id"),
        barril_7_8_9_litros=1,
        barril_10_12_litros=1
    )

    session.add(test_comodato)
    session.commit()
    session.refresh(test_comodato)

    #  2) creamos un request body vacío para que el validador ingrese valores por default
    request_body = {}

    response = client.put(
        f"/comodatos/{test_comodato.id}", json=request_body)

    assert response.status_code == 200

    #  3) una vez actualizado, recuperamos el registro
    comodato_db = session.query(models.Comodato).filter(
        models.Comodato.id == test_comodato.id).first()

    #  4) mapeamos por el schema correspondiente los valores de la base de datos con los del response.json()
    comodato_schema = comodatos.ComodatoOut(**comodato_db.__dict__)
    comodato_output = comodatos.ComodatoOut(**response.json())

    #  3) Comparamos ambos schemas
    assert comodato_output == comodato_schema


def test_delete_comodato(client, session, body_comodato):
    # Create a new comodato in the database

    comodato = models.Comodato(**body_comodato)
    session.add(comodato)
    session.commit()
    session.refresh(comodato)

    # Send a DELETE request to the /comodatos/{comodato_id} path with the comodato ID
    response = client.delete(f"/comodatos/{comodato.id}")

    # Check the response status code and content
    assert response.status_code == 204

    # Send a DELETE request to the /comodatos/{comodato_id} path with an invalid comodato ID
    response = client.delete("/comodatos/999")

    # Check the response status code and content
    assert response.status_code == 404
    assert response.json() == {"detail": "Comodato not found"}
