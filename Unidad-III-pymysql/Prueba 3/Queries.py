# Evaluación 3 - Camilo Riquelme
# Bases de Datos - Prof. Alex Slater

import pymysql
from beautifultable import BeautifulTable
from os import system

class DAO:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bdmp3')
        self.cursor = self.connection.cursor()
        system('cls')
        print('Conexión establecida exitosamente.') 
        print('Se procederá a ejecutar las consultas. \n')
        system('pause')
        system('cls')

    def Consulta1(self):
        sql = 'select d.first_name as nombre, d.last_name as apellido, count(md.movie_id) as cant_peliculas from directors as d join movies_directors as md on d.id = md.director_id group by d.id, d.first_name, d.last_name having count(md.movie_id)>3 order by cant_peliculas desc;'
        try:
            self.cursor.execute(sql)
            directores = self.cursor.fetchall()
            return directores
        except Exception as e:    
            print(f'Error al ejecutar consulta. Error: {e}')

    def Consulta2(self):
        sql = 'select a.first_name as nombre, a.last_name as apellido, count(ma.movie_id) as cant_peliculas from actors as a join movies_actors as ma on a.id = ma.actor_id group by a.id order by apellido asc;'
        try:
            self.cursor.execute(sql)
            actores = self.cursor.fetchall()
            return actores
        except Exception as e:    
            print(f'Error al ejecutar consulta. Error: {e}')

    def Consulta3(self):
        sql = 'select m.name as pelicula, m.year as año, d.first_name as nombre_director, d.last_name as apellido_director, m.rank as puntaje from movies as m join movies_directors as md on m.id=md.movie_id join directors as d on md.director_id=d.id where m.rank>8 order by m.rank desc;'
        try:
            self.cursor.execute(sql)
            peliculas = self.cursor.fetchall()
            return peliculas
        except Exception as e:    
            print(f'Error al ejecutar consulta. Error: {e}')

# Programa principal

d = DAO()

dr=d.Consulta1()
ac=d.Consulta2()
pe=d.Consulta3()

# Revisión de formato de datos

# print(dr)
# print(ac)
# print(pe)

tabla1 = BeautifulTable()
for d in dr:
    x = [d[0], d[1], str(d[2])] # Se pasaron a string formatos numéricos
    tabla1.rows.append(x)
tabla1.columns.header = ['NOMBRE DIRECTOR', 'APELLIDO DIRECTOR', 'CANTIDAD DE PELICULAS']
print(f'CONSULTA 1: \n\n {tabla1} \n\n Seguir a consulta 2. \n')
system('pause')
system('cls')

tabla2 = BeautifulTable()
for a in ac:
    x = [a[0], a[1], str(a[2])] # Se pasaron a string formatos numéricos
    tabla2.rows.append(x)
tabla2.columns.header = ['NOMBRE ACTOR', 'APELLIDO ACTOR', 'CANTIDAD DE PELICULAS']
print(f'CONSULTA 2: \n\n {tabla2} \n\n Seguir a consulta 3. \n')
system('pause')
system('cls')

tabla3 = BeautifulTable()
for p in pe:
    x = [p[0], str(p[1]), p[2], p[3], float(p[4])] # Se pasaron a string formatos numéricos
    tabla3.rows.append(x)
tabla3.columns.header = ['PELICULA', 'AÑO', 'NOMBRE DIRECTOR', 'APELLIDO DIRECTOR', 'PUNTAJE']
print(f'CONSULTA 3 \n\n {tabla3} \n\n Programa terminado. \n')
system('pause')
system('cls')
