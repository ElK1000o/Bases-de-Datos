import pymysql

class DAO: # Data Access Object

    def __init__(self):

        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bd4')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente. ') # Opcional

    def InsertarTallas(self):
        try:
            id = int(input("\nDigite Id    : "))
            nom = input("Digite Talla : ");
            val = (id,nom)
            sql = "insert into tallas (id_tal, nom_tal) values (%s, %s)"        
            self.cursor.execute(sql, val)
            self.connection.commit()
            print("\n--- Talla Insertada Correctamente!! ---\n")
            system("pause")
        except Exception:
            print("Error Al Intentar Insertar Talla!!")

    def ListarTallas(self):
        sql = "select * from tallas"
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            i = 1
            print("\n--- LISTADO ---")
            for x in rs:
                print("Talla ",i," :",x)
                i += 1
            system("pause")
        except Exception:
            print("Error Al Obtener Tallas!!")

def menu():
    while True:
        system("cls")
        print("\n--- MENU ---")
        print("1.Insertar Marcas")
        print("2.Listar Marcas")
        print("3.Salir")
        op = int(input("Digite Una Opcion : "))
        if op!=1 and op!=2:
            print("\n--- Error De Opcion!! ---")
            system("pause")
        else:
            if op==1:
                d.InsertarTallas()
            elif op==2:
                d.ListarTallas()
            elif op==3:
                break

from os import system
system("cls")

# Programa Principal

d = DAO()
menu()
