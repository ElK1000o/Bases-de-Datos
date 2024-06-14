# Evaluación 4 - Camilo Riquelme
# Bases de Datos - Prof. Alex Slater
# f1data

import json 
import pymysql
import requests
from os import system

class DAO:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='f1data')
        self.cursor = self.connection.cursor()
        system('cls')
        print('Conexión establecida') 
        system('pause')
        system('cls')

    def CargarDatos(self, lista):
        for dato in lista: 
            try:
                sql = '''
                    INSERT INTO results (season, raceName, number, 
                                        position, points, constructor) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                    '''
                val = (dato.getSeason(), dato.getNombre(), dato.getNumber(), 
                       dato.getPosition(), dato.getPoints(), dato.getConstructor())    
                self.cursor.execute(sql, val)
                self.connection.commit()
            except Exception as e:
                print(f"Error al insertar dato: {e}")
                print(f"Datos: {dato.getSeason()}, {dato.getNombre()}, {dato.getNumber()}, {dato.getPosition()}, {dato.getPoints()}, {dato.getConstructor()}")

class Dato:
    def __init__(self):
        self.nom = ""
        self.temp = ""
        self.num = ""
        self.pos = ""
        self.pts = ""
        self.cons = ""

    def setSeason(self, temp):
        self.temp = temp

    def setNombre(self, nom):
        self.nom = nom
    
    def setNumber(self, num):
        self.num = num
    
    def setPosition(self, pos):
        self.pos = pos

    def setPoints(self, pts):
        self.pts = pts

    def setConstructor(self, cons):
        self.cons = cons
    
    def getSeason(self):
        return self.temp
    
    def getNombre(self):
        return self.nom
    
    def getNumber(self):
        return self.num
    
    def getPosition(self):
        return self.pos

    def getPoints(self):
        return self.pts

    def getConstructor(self):
        return self.cons

# PROGRAMA PRINCIPAL

d = DAO()

webs = [
    'https://ergast.com/api/f1/2018/results.json',
    'https://ergast.com/api/f1/2019/results.json',
    'https://ergast.com/api/f1/2020/results.json',
    'https://ergast.com/api/f1/2021/results.json',
    'https://ergast.com/api/f1/2022/results.json'
]

datos = []

for web in webs:
    respuesta = requests.get(web)
    if respuesta.status_code == 200: # Comprobamos que la respuesta fue exitosa y no hay errores en ninguna URL
        data = json.loads(respuesta.text)
        for race in data['MRData']['RaceTable']['Races']:
            raceName = race['raceName']
            season = race['season']
            for result in race['Results']:
                dato_obj = Dato()
                dato_obj.setNombre(raceName)
                dato_obj.setSeason(season)
                dato_obj.setNumber(result['number'])
                dato_obj.setPosition(result['position'])
                dato_obj.setPoints(result['points'])
                dato_obj.setConstructor(result['Constructor']['name'])
                datos.append(dato_obj)
    else:
        print(f"Error al acceder a la URL: {web}")

try:
    d.CargarDatos(datos)
    print('Datos ingresados exitosamente \n\n')
except:
    print('\n\n No se lograron cargar los datos \n\n')
system('pause')
system('cls')
