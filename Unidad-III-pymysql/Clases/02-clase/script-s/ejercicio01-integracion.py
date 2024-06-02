import pymysql
import csv
import os

class DAO:  # Data Access Object

    def __init__(self):
        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='clase2')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente.')  # Opcional

    def InsertarDatos(self, filas):
        sql = 'INSERT INTO comunas(codigo, nombre, telefono) VALUES (%s, %s, %s)'
        try:
            self.cursor.executemany(sql, filas)
        except Exception as e:
            print(f'Error al ejecutar consulta. Error: {e}')
        self.connection.commit()

# PROGRAMA PRINCIPAL
# Leeremos el CSV para recuperar los datos, después los cargaremos en el BD XAMPP MySQL

d = DAO()

# Ruta al archivo CSV

data_dr = os.path.dirname(__file__)
csv_path = os.path.join(data_dr, '..', 'data', 'comunas2.csv')

with open(csv_path, 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')
    filas = []
    first = next(readCSV)  # Salta la primera línea
    for row in readCSV:
        # print(row)
        # agregar cada row como tupla a la lista de filas
        filas.append(tuple([row[0], row[1], row[2]]))

# Insertar datos

d.InsertarDatos(filas)