import pytest
from .database import client, session
# import schema validator: from app.schemas import clientes


# # write your tests here
# def test_get_all_clientes(client):
#     res = client.get("/v1/clientes/")

#     def validate(premio):
#         return clientes.Premio(**premio)
#     posts_map = map(validate, res.json())
#     posts_list = list(posts_map)
#     assert res.status_code == 200



# def test_get_one_premio_not_exist(client):
#     res = client.get(f"/v1/premios/88888")
#     assert res.status_code == 404