import datetime
import requests


def create_recibo(data):
    # Send a POST request to the /recibos path with the JSON data
    response = requests.post("http://localhost:8000/recibos", json=data[0])

    # Check the response status code and content
    if response.status_code == 201:
        print("Recibo created successfully!")
        print(response.json())
    else:
        print(f"Error creating recibo: {response.status_code}")
        print(response.json())


def update_recibo(id):
    # Send a PUT request to the /recibos path with the JSON data
    data = {
      "monto_recibo": 20000,
    }

    response = requests.put(f"http://localhost:8000/recibos/{id}", json=data)

    # Check the response status code and content
    if response.status_code == 200:
        print("Recibo updated successfully!")
        print(response.json())
    else:
        print(f"Error updating recibo: {response.status_code}")
        print(response.json())


def delete_recibo(id):
    # Send a DELETE request to the /recibos path with the JSON data
    response = requests.delete(f"http://localhost:8000/recibos/{id}")

    # Check the response status code and content
    if response.status_code == 204:
        print(f"Recibo deleted successfully!")
    else:
        print(f"Error deleting recibos: {response.status_code}")


def get_all_recibos():
    # Send a GET request to the /recibos path with the JSON data
    response = requests.get(f"http://localhost:8000/recibos/")

    # Check the response status code and content
    if response.status_code == 200:
        print(f"recibos retrieved successfully!")
        print(response.json())
    else:
        # print('\nresponse:\n', dir(response)[-25:],'\n')
        # print('\nresponse ok:\n', response.ok,'\n')
        # print('\nresponse text\n', response.text,'\n')
        # print('\nresponse json\n', response.reason,'\n')
        print(f"Error retrieving recibos: {response.status_code}")


def read_recibo(id):
    # Send a GET request to the /recibos path with the JSON data
    response = requests.get(f"http://localhost:8000/recibos/{id}")

    # Check the response status code and content
    if response.status_code == 200:
        print(f"recibos retrieved successfully!")
        print(response.json())
    else:
        print(f"Error retrieving recibos: {response.status_code}")


def seed_recibos():
    def crear_cliente():
        data = [
            {
                "dni": "12365478",
                "nombre": "Juan",
                "apellido": "Perez",
                "direccion": "Calle 123",
                "barrio": "Palermo",
                "localidad": "CABA",
                "telefono": "123-44567890",
                "email": "cliente@test.com",
                "vehiculo": "Fiat 147",
                "patente": "ABC123",
                "fecha_cumple": "12/12/1990",
            }
        ]
        response = requests.post("http://localhost:8000/clientes", json=data[0])

        # Check the response status code and content
        if response.status_code == 201:
            print(f"Cliente created successfully!")
        else:
            print(f"Error creating cliente")

        return response.json()

    def crear_comodato(cliente_id):
        data = [
            {
                "cliente_id": cliente_id,
                "barril_18_litros": 1,
            }
        ]
        response = requests.post("http://localhost:8000/comodatos", json=data[0])

        # Check the response status code and content
        if response.status_code == 201:
            print(f"Comodato created successfully!")
        else:
            print(f"Error creating comodato")

        return response.json()

    
    def buscar_cliente_dni(dni):
        response = requests.get(f"http://localhost:8000/clientes/dni/", params=f"cliente_dni={dni}")

        # Check the response status code and content
        if response.status_code == 200:
            print(f"Cliente retrieved successfully!")
        else:
            print(f"Error retrieving cliente")

        return response.json()
    
    try:
        cliente = buscar_cliente_dni("12365478")
        comodato = crear_comodato(int(cliente["id"]))
    except:
        cliente = crear_cliente()
        comodato = crear_comodato(cliente["id"])
    

    data = [
        {
            "monto_recibo": 2000,
            "cliente_id": cliente["id"],
            "comodato_id": comodato["id"],
        }
    ]
    create_recibo(data)


def main():
    seed_recibos()
    # update_recibo(3)
    # delete_recibo(3)
    get_all_recibos()
    print("="*150)
    read_recibo(1)


if __name__ == "__main__":
    main()
