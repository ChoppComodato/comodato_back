# import csv
# import concurrent.futures
# from itertools import count
import datetime
import requests


def create_comodato():
    # Send a POST request to the /comodatos path with the JSON data
    data = [
        {
            "barril_7_8_9_litros": 1,
            "barril_10_12_litros": 1,
            "barril_18_litros": 1,
            "barril_25_litros": 1,
            "barril_30_litros": 1,
            "barril_40_50_litros": 1,
            "choppera_sin_barril": 1,
            "reductor_presion": 1,
            "tubo_CO2": 1,
            "peso_tubo_CO2": 1,
            "valvula_automatica": 1,
            "cabezal_10_litros": 1,
            "adicionales": "test1",
            "observaciones": "test1000000"
        }
    ]

    response = requests.post("http://localhost:8000/comodatos", json=data[0])

    # Check the response status code and content
    if response.status_code == 201:
        print(f"Comodatos created successfully!")
        print(response.json())
    else:
        print(f"Error creating comodatos: {response.status_code}")


def main():
    create_comodato()


if __name__ == '__main__':
    main()
