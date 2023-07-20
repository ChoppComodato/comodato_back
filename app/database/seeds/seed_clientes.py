import csv
import httpx
import concurrent.futures
from itertools import count
import datetime
import requests


counter = count(start=1, step=1)


def send_request(data):
    # Send a POST request to the /clientes path with the JSON data
    response = requests.post("http://localhost:8000/clientes", json=data[0])

    # Check the response status code and content
    if response.status_code == 201:
        print(f"Clientes [{next(counter)}] created successfully!")
    else:
        print(f"Error creating clientes [{next(counter)}]: {response.status_code}")


def modificar_formato_fecha(diccionario):
    fecha_cumple = diccionario.get('fecha_cumple', None)
    if fecha_cumple is None:
        return diccionario

    partes_fecha = fecha_cumple.split('/')
    if len(partes_fecha) != 3:
        return diccionario

    mes, dia, anio = partes_fecha
    nueva_fecha = f"{dia}/{mes}/{anio}"
    diccionario['fecha_cumple'] = nueva_fecha
    return diccionario


def modificar_formato_dni(diccionario):
    dni = diccionario.get('dni', None)
    if dni is None:
        return diccionario

    dni = int(dni)
    diccionario['dni'] = dni
    return diccionario


def main():

    # Open the CSV file and read the data
    with open("MOCK_DATA_CLIENTES.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, skipinitialspace=True)
        data = [row for row in reader]

    # Modify the date format
    data = [modificar_formato_fecha(row) for row in data]
    # Convert the dni to int
    data = [modificar_formato_dni(row) for row in data]

    # # create a MANUAL instance of the post requests
    # for i, row in enumerate(data):
    #     if i == 4:
    #         print(f"{row}")
    #         response = requests.post(
    #             "http://localhost:8000/clientes", json=row)
    #         print(response.json())
    #         break

    # Create a ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        futures = [executor.submit(send_request, [row]) for row in data]
        concurrent.futures.wait(futures)


if __name__ == "__main__":
    main()
