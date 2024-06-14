import json
import requests
from beautifultable import BeautifulTable

# Vamos a leer una API en JSON y trabajar con ella un programa en Python

# Hacer request al servidor

respuesta = requests.get('https://jsonplaceholder.typicode.com/todos')
print(respuesta) # Se genera un objeto de tipo request

# Deserealizar el JSON recibido en la respuesta

dicc = json.loads(respuesta.text) # se saca el texto del objeto tipo request y se deserealiza el JSON

# print(dicc)

# print(type(dicc)) # evaluamos el tipo devuelto

# for d in dicc: 
#     print(d) # Imprimimos cada diccionario

# for d in dicc: # Imprimimos cada dato del diccionario
#     print(f'User ID: {d["userId"]}')
#     print(f'ID: {d["id"]}')
#     print(f'Titulo: {d["title"]}')
#     print(f'Completado: {d["completed"]}')  # Valor del diccionario en comillas dobles

tabla = BeautifulTable()
tabla.columns.header = ['User ID', 'ID', 'Titulo']

for d in dicc: # Visualizar en tabla con BeautifulTable 
    tabla.rows.append([str(d["userId"]), str(d["id"]), d["title"]])

print(tabla)

