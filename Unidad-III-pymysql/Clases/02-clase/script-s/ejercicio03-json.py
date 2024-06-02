import json

datos_JSON = """
{ 
	"tamano": "mediana",
	"precio": 15.67,
	"toppings": ["champinones", "pepperoni", "albahaca"],
	"queso_extra": false,
	"delivery": true,
	"cliente": {
		"nombre": "Jane Doe",
		"telefono": null,
		"correo": "janedoe@email.com"
	}
}
"""

diccionario = json.loads(datos_JSON) # Deserealizar JSON

# Corroborar el diccionario desdde Python

print(diccionario['tamano'])
print(diccionario['toppings'])
print(diccionario['cliente'])

cliente = {
    "nombre": "Nora",
    "edad": 56,
    "id": "45355",
    "color_ojos": "verdes",
    "usa_lentes": False
}

print(cliente, '\n')
print('Acá serialziado: ')

json_salida = json.dumps(cliente)
print(json_salida)

# Se produce cambio de comillas simples a dobles (JSON no acepta comillas simples), se cambia False por false
