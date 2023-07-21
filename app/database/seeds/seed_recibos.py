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
        "monto_recibo": 2000
    }

    response = requests.put(f"http://localhost:8000/recibos/{id}", json=data)

    # Check the response status code and content
    if response.status_code == 200:
        print("Recibo updated successfully!")
        print(response.json())
    else:
        print(f"Error updating recibo: {response.status_code}")
        print(response.json())



#TODO:



def main():
    # create_recibo()
    update_recibo(5)


main()
