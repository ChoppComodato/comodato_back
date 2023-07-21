import datetime
import requests


def create_recibo():
    # Send a POST request to the /recibos path with the JSON data
    data = [
        {
            "monto_recibo": 1000,
            "cliente_id": 1,
            "comodato_id": 1
        }
    ]

    response = requests.post("http://localhost:8000/recibos", json=data[0])

    # Check the response status code and content
    if response.status_code == 201:
        print("Recibo created successfully!")
        print(response.json())
    else:
        print(f"Error creating recibo: {response.status_code}")


def update_recibo(id):
    # Send a PUT request to the /recibos path with the JSON data
    data = {
        "cliente_id": 40,
        "comodato_id": 5
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


def main():
    # create_recibo()
    # update_recibo(5)
    # delete_recibo(3)
    get_all_recibos()
    print("="*150)
    read_recibo(1)


if __name__ == "__main__":
    main()
