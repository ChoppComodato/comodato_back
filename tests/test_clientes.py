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


# def test_get_one_premio_not_exist(client):
#     res = client.get(f"/v1/premios/88888")
#     assert res.status_code == 404

    # Check that the response status code is 204
    assert response.status_code == 204