import pymysql

class DAO: # Data Access Object

    def __init__(self):

        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bd3')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente. ') # Opcional

    def ListarModelo(self):
        sql = 'select * from modelos'
        try:
            self.cursor.execute(sql) # Ejecutar consulta
            rs = self.cursor.fetchall() # Recuperar datos
            # print('Resultado consulta: ', rs)
            return rs
        except Exception as e:
            print('Error al ejecutar consulta. ' f'Error: {e}')

    def InsertarModelo(self):
        try:
            id = int(input("Digite ID De Modelo: "))
            nom = input('Escriba el nombre de la marca: ')
            val = (id, nom) # Tupla de valores
            sql = 'insert into modelos (id_mod, nom_mod) values (%s, %s)'
            self.cursor.execute(sql, val)
            self.connection.commit() # Importante o no se graban los datos.
            print('Marca agregada correctamente. ')

        except Exception as e:
            print('Error al ejecutar consulta. ' f'Error: {e}')

from os import system
system("cls")

# Programa Principal

d = DAO()

d.InsertarModelo()
d.ListarModelo()