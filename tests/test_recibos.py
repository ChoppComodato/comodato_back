from app.src.schemas import comodatos, recibos
from app.database import models


def test_post_recibo(client, test_cliente, test_comodato):
    recibo_data = {
        "cliente_id": test_cliente["id"],
        "comodato_id": test_comodato["id"],
        "monto_recibo": 1000
    }

    response = client.post("/recibos/", json=recibo_data)
    print('\n', response.json(), '\n')
    print(f'status code: {response.status_code}\n')
    assert response.status_code == 201


def test_get_all_recibos(client):
    res = client.get("/recibos/")

    def validate(row):
        return recibos.ReciboOut(**row)

    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    assert res.status_code == 200


def test_get_one_recibo(client, session, test_recibo):

    # Make a request to the read_recibo endpoint
    response = client.get(f"/recibos/{test_recibo.get('id')}")

    # Validate the response
    assert response.status_code == 200
    assert response.json()["id"] == test_recibo.get("id")
    assert response.json()["cliente_id"] == test_recibo.get("cliente_id")
    assert response.json()["comodato_id"] == test_recibo.get("comodato_id")
    assert response.json()["monto_recibo"] == test_recibo.get("monto_recibo")


def test_update_recibo(client, session, test_recibo):
    # Define a new recibo
    new_recibo = {
        "cliente_id": test_recibo.get("cliente_id"),
        "comodato_id": test_recibo.get("comodato_id"),
        "monto_recibo": 2000
    }

    # Make a request to the update_recibo endpoint
    response = client.put(
        f"/recibos/{test_recibo.get('id')}", json=new_recibo)

    # Validate the response
    assert response.status_code == 200
    assert response.json()["id"] == test_recibo.get("id")
    assert response.json()["cliente_id"] == test_recibo.get("cliente_id")
    assert response.json()["comodato_id"] == test_recibo.get("comodato_id")
    assert response.json()["monto_recibo"] == 2000


def test_delete_recibo(client, session, test_recibo):
    # Make a request to the delete_recibo endpoint
    response = client.delete(f"/recibos/{test_recibo.get('id')}")

    # Validate the response
    assert response.status_code == 204


def test_get_one_recibo_not_found(client, session):
    # Make a request to the read_recibo endpoint
    response = client.get("/recibos/999")

    # Validate the response
    assert response.status_code == 404
    assert response.json()["detail"] == "Recibo not found"


def test_update_recibo_not_found(client, session):
    # Define a new recibo
    new_recibo = {
        "cliente_id": 1,
        "comodato_id": 1,
        "monto_recibo": 2000
    }

    # Make a request to the update_recibo endpoint
    response = client.put("/recibos/999", json=new_recibo)

    # Validate the response
    assert response.status_code == 404
    assert response.json()["detail"] == "Recibo 999 no encontrado"


def test_delete_recibo_not_found(client, session):
    # Make a request to the delete_recibo endpoint
    response = client.delete("/recibos/999")

    # Validate the response
    assert response.status_code == 404
    assert response.json()["detail"] == "Recibo 999 no encontrado"


def test_post_recibo_not_found(client, session):
    recibo_data = {
        "cliente_id": 1,
        "comodato_id": 1,
        "monto_recibo": 1000
    }

    response = client.post("/recibos/", json=recibo_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Cliente 1 no encontrado"
