import csv
import httpx
import concurrent.futures
from itertools import count
import datetime


counter = count(start=1, step=1)


def send_request(data):
    # Send a POST request to the /clientes path with the JSON data
    response = httpx.post("http://localhost:8000/clientes", json=data)

    # Check the response status code and content
    if response.status_code == 200:
        print(f"Clientes [{next(counter)}] created successfully!")
    else:
        print(f"Error creating clientes [{next(counter)}]: {response.content}")


# Open the CSV file and read the data
with open("MOCK_DATA_CLIENTES.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, skipinitialspace=True)
    data = [row for row in reader]


def main():
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


    # create a manual instance of the post requests
    for i, row in enumerate(data):
        row['dni'] = int(row['dni'])
        row['fecha_cumple'] = modificar_formato_fecha(row)['fecha_cumple']

        response = httpx.post("http://localhost:8000/clientes", json=row)

        if i == 1:
            break


    print("\n\n\tPROGRAMA PRINCIPAL\n")
    # print("atributos de httpx.Response")
    # print(dir(response)[-20:])
    # print("\n")
    # print("objeto httpx.Response.request")
    # print(response.request)
    # print("\n")
    # print("objeto httpx.Response.text")
    # print(response.text)
    # print("\n")
    # print("objeto httpx.Response.status_code")
    # print(response.status_code)
    # print("\n")
    print(f"row es {row}")




main()


# # Create a ThreadPoolExecutor
# with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
#     futures = [executor.submit(send_request, [row]) for row in data]
#     concurrent.futures.wait(futures)
