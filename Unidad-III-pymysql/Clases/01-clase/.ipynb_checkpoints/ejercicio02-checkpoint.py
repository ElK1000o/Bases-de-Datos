import pymysql

class DAO: # Data Access Object

    def __init__(self):

        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bd2')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente. ') # Opcional

    def ListarMarcas(self):
        sql = 'select * from marcas'
        try:
            self.cursor.execute(sql) # Ejecutar consulta
            rs = self.cursor.fetchall() # Recuperar datos
            # print('Resultado consulta: ', rs)
            return rs
        except Exception as e:
            print('Error al ejecutar consulta. ' f'Error: {e}')

    def InsertarMarca(self):
        try:
            nom = input('Escriba el nombre de la marca: ')
            val = (nom) # Tupla de valores
            sql = 'insert into marcas (nom_mar) values (%s)'
            self.cursor.execute(sql, val)
            self.connection.commit() # Importante o no se graban los datos.
            print('Marca agregada correctamente. ')

        except Exception as e:
            print('Error al ejecutar consulta. ' f'Error: {e}')

from os import system
system("cls")

# Programa Principal

d = DAO()

print("--- LISTADO DE MARCAS ---")
rs = d.ListarMarcas()
for r in rs:
    print(f'ID Marca: {r[0]}')
    print(f'Nombre Marca: {r[1]}')

d.InsertarMarca()
print("--- LISTADO ACTUALIZADO DE MARCAS ---")
rs = d.ListarMarcas()
for r in rs:
    print(f'ID Marca: {r[0]}')
    print(f'Nombre Marca: {r[1]}')
