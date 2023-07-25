# import csv
# import concurrent.futures
# from itertools import count
import datetime, requests, random


def create_comodato(data):
    # Send a POST request to the /comodatos path with the JSON data
    response = requests.post("http://localhost:8000/comodatos", json=data[0])

    # Check the response status code and content
    if response.status_code == 201:
        print(f"Comodatos created successfully!")
        print(response.json())
    else:
        print(f"Error creating comodatos: {response.status_code}")



def update_comodato(id):
    "Update Comodato: la actualización de las variables se hace por default desde el validador de pydantic"
    # Send a PUT request to the /comodatos path with the JSON data
    response = requests.put(f"http://localhost:8000/comodatos/{id}", json={})

    # Check the response status code and content
    if response.status_code == 200:
        print(f"Comodatos updated successfully!")
        print(response.json())
    else:
        print(f"Error updating comodatos: {response.status_code}")
        print(response.json())


def delete_comodato(id):
    # Send a DELETE request to the /comodatos path with the JSON data
    response = requests.delete(f"http://localhost:8000/comodatos/{id}")

    # Check the response status code and content
    if response.status_code == 204:
        print(f"Comodatos deleted successfully!")
    else:
        print(f"Error deleting comodatos: {response.status_code}")

def get_comodato(id):
    # Send a GET request to the /comodatos path with the JSON data
    response = requests.get(f"http://localhost:8000/comodatos/{id}")

    # Check the response status code and content
    if response.status_code == 200:
        print(f"Comodatos retrieved successfully!")
        print(response.json())
    else:
        print(f"Error retrieving comodatos: {response.status_code}")

def read_comodatos():
    # Send a GET request to the /comodatos path with the JSON data
    response = requests.get(f"http://localhost:8000/comodatos/")

    # Check the response status code and content
    if response.status_code == 200:
        print(f"Comodatos retrieved successfully!")
        print(response.json())
    else:
        print(f"Error retrieving comodatos: {response.status_code}")


def main():
    data = [
        {
            "cliente_id": random.randint(1, 100),
            "barril_7_8_9_litros": 2,
            # "barril_10_12_litros": 1,
            # "barril_18_litros": 1,
            # "barril_25_litros": 1,
            # "barril_30_litros": 1,
            # "barril_40_50_litros": 1,
            # "choppera_sin_barril": 1,
            # "reductor_presion": 1,
            # "tubo_CO2": 1,
            # "peso_tubo_CO2": 1,
            "valvula_automatica": 1,
            "cabezal_10_litros": 1,
            # "adicionales": "test2",
            "observaciones": "Sin observaciones"
        }
    ]

    # create_comodato(data)
    # update_comodato(4)
    # delete_comodato(3)
    get_comodato(1)
    print('='*50)
    read_comodatos()

if __name__ == '__main__':
    main()
