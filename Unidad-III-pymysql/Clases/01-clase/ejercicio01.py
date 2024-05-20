import pymysql

class DAO: # Data Access Object

    def __init__(self):

        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bd1')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente. ') # Opcional

    # Aqui vamos a ir definiendo otros métodos para interactuar con la BD    
    def ListarMascotas(self):
        sql = 'select * from mascotas'
        try:
            self.cursor.execute(sql) # Ejecutar consulta
            rs = self.cursor.fetchall() # Recuperar datos
            # print('Resultado consulta: ', rs)
            return rs
        except:    
            print('Error al ejecutar consulta. ')

    def InsertarMascota(self):
        try:
            nom = input('Escriba el nombre de la mascota: ')
            eda = int(input('Digite la edad de la mascota: '))
            val = (nom, eda) # Tupla de valores
            sql = 'insert into mascotas (nom_mas, eda_mas) values (%s, %s)'
            self.cursor.execute(sql, val)
            self.connection.commit() # Importante o no se graban los datos.
            print('Mascota agregada correctamente. ')

        except Exception as e:
            print('Error al ejecutar consulta. ' f'Error: {e}')

from os import system
system("cls")

# Programa Principal

d = DAO()
d.ListarMascotas()
rs = d.ListarMascotas()

d.InsertarMascota()
print('--- NUEVA LISTA DE MASCOTAS ACTUALIZADA ---')

# Presentar listado de mascotas
print(rs)
for r in rs:
    print(f'ID Mascota: {r[0]}')
    print(f'Nombre Mascota: {r[1]}')
    print(f'Edad Mascota: {r[2]}')
