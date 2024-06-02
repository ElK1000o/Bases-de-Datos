from beautifultable import BeautifulTable

tabla = BeautifulTable() # Crea objeto BeautifulTable para crear tablas.

# Agregar fila a tabla

tabla.rows.append(['1', 'Juan', 'Perez']) # Todo se recibe como string
tabla.rows.append(['2', 'Pedro', 'Rodriguez'])
tabla.rows.append(['3', 'El', 'Pailita'])

# Agregar Header

tabla.columns.header = ['ID', 'NOMBRE', 'APELLIDO']

# Mostrar tabla

print(tabla)
