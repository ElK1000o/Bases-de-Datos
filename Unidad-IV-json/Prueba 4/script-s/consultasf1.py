# Evaluación 4 - Camilo Riquelme
# Bases de Datos - Prof. Alex Slater
# Consultas

import pymysql
from beautifultable import BeautifulTable
from os import system

class DAO:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='f1data')
        self.cursor = self.connection.cursor()
        system('cls')
        print('Conexión establecida exitosamente.') 
        print('Se procederá a ejecutar las consultas. \n')
        system('pause')
        system('cls')

    def Consulta1(self):
        sql = '''
            SELECT season, raceName, number, position, points, constructor
            FROM results
            WHERE season = 2019 AND position IN (1, 2, 3);
            '''
        try:
            self.cursor.execute(sql)
            x = self.cursor.fetchall()
            return x
        except Exception as e:    
            print(f'Error al ejecutar consulta 1. Error: {e}')

    def Consulta2(self):
        sql = '''
            SELECT season, constructor, SUM(points) as pts
            FROM results
            GROUP BY season, constructor;
            '''
        try:
            self.cursor.execute(sql)
            y = self.cursor.fetchall()
            return y
        except Exception as e:    
            print(f'Error al ejecutar consulta 2. Error: {e}')

    def Consulta3(self):
        sql = '''
            SELECT number, SUM(points) as pts
            FROM results
            WHERE season BETWEEN 2018 AND 2022
            GROUP BY number
            ORDER BY pts DESC
            LIMIT 5;
            '''
        try:
            self.cursor.execute(sql)
            z = self.cursor.fetchall()
            return z
        except Exception as e:    
            print(f'Error al ejecutar consulta 3. Error: {e}')

# Programa principal

d = DAO()

ax = d.Consulta1()
bx = d.Consulta2()
cx = d.Consulta3()

# Revisión de formato de datos

# print(ax)
# print(bx)
# print(cx)

tabla1 = BeautifulTable()
for a in ax:
    x = [str(a[0]), a[1], str(a[2]), str(a[3]), str(a[4]), a[5]] 
    tabla1.rows.append(x)
tabla1.columns.header = ['TEMPORADA', 'CARRERA', 'PILOTO', 'POSICION', 'PUNTOS', 'CONSTRUCTOR']
print(f'CONSULTA 1: \n\n {tabla1} \n\n Seguir a consulta 2. \n')
system('pause')
system('cls')

tabla2 = BeautifulTable()
for b in bx:
    x = [str(b[0]), b[1], str(b[2])] 
    tabla2.rows.append(x)
tabla2.columns.header = ['TEMPORADA', 'CONSTRUCTOR', 'PUNTOS TOTALES']
print(f'CONSULTA 2: \n\n {tabla2} \n\n Seguir a consulta 3. \n')
system('pause')
system('cls')

tabla3 = BeautifulTable()
for c in cx:
    x = [str(c[0]), str(c[1])] 
    tabla3.rows.append(x)
tabla3.columns.header = ['PILOTO', 'PUNTOS TOTALES']
print(f'CONSULTA 3 \n\n {tabla3} \n\n Programa terminado. \n')
system('pause')
system('cls')
