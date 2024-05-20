import pymysql

class DAO: # Data Access Object

    def __init__(self):

        # Conector para iniciar las credenciales de conexión
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          db='bd5')
        
        # Crear un cursor (Ejecutar instrucciones)
        self.cursor = self.connection.cursor()
        print('Conexión establecida exitosamente. ') # Opcional

    def InsertarNacionalidades(self):
        try:
            id = int(input("\nDigite Identificador : "))
            nac = input("Digite Nacionalidad  : ");
            abr = input("Digite Abreviatura   : ");
            val = (id,nac,abr)
            sql = "insert into nacionalidades (id_nac, nom_nac, abr_nac) values (%s, %s, %s)"        
            self.cursor.execute(sql, val)
            
            op = int(input("\n¿Desea Agregar Nacionalidad? (1.Si  2.No) : "))
            if op==1:
                self.connection.commit()
                print("\n--- Nacionalidad Agregada Correctamente!! ---\n")
            elif op==2:
                self.connection.rollback()
                print("\n--- Se Deshizo La Acción!! ---\n")
            system("pause")
        except Exception:
            print("Error Al Intentar Agregar Nacionalidad!!")

    def ListarNacionalidades(self):
        sql = "select * from nacionalidades"
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            i = 1
            print("\n--- LISTADO ---")
            for x in rs:
                print("Nacionalidad ",i," :",x)
                i += 1
            system("pause")
        except Exception:
            print("Error Al Obtener Nacionalidades!!")

def menu():
    while True:
        system("cls")
        print("\n--- MENU ---")
        print("1.Insertar Nacionalidades")
        print("2.Listar Nacionalidades")
        print("3.Salir")
        op = int(input("Digite Una Opcion : "))
        if op!=1 and op!=2 and op!=3:
            print("\n--- Error De Opcion!! ---")
            system("pause")
        else:
            if op==1:
                d.InsertarNacionalidades()
            elif op==2:
                d.ListarNacionalidades()
            elif op==3:
                break

from os import system
system("cls")

# Programa Principal

d = DAO()
menu()
