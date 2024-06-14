import pymysql
import json
import requests
from os import system

class DAO:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='clasejson')
        self.cursor = self.connection.cursor()
        system('cls')
        print('Conexión establecida exitosamente.') 
        print('Se procederá a ejecutar las consultas. \n')
        system('pause')
        system('cls')

    def InsertarDato(self, lista):
        for c in lista: # C -> Objeto clase color
            try:
                sql = "insert into colores (color, valor) values (%s, %s)"    
                val = (c.getNombre(), c.getValor())    
                self.cursor.execute(sql, val)
                self.connection.commit()
            except:
                print(f"Error al insertar dato! {c.getNombre()}, {c.getValor()}")

class color:
    def __init__(self):
        self.nombre = ""
        self.valor = ""
    # Crearemos metodos GET y SET
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setValor(self, valor):
        self.valor = valor
    
    def getNombre(self):
        return self.nombre
    
    def getValor(self):
        return self.valor

# Programa principal
d = DAO()

# Recuperamos datos de la API y deserealizamos

resp = requests.get('https://raw.githubusercontent.com/bahamas10/css-color-names/master/css-color-names.json')

resp = json.loads(resp.text)

# Crear lista de objetos color para almacenar lo recibido

colores = []

for r in resp.keys():
    nombre = r
    valor = resp[r]
    c = color()
    c.setNombre(nombre) # o r
    c.setValor(valor) # o resp[r]
    colores.append(c)

d.InsertarDato(colores)