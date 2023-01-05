# Creando un diccionario vacio
diccionario = {}
#print(diccionario)
#print(type(diccionario))


# Asignar valores a nuestro diccionario
diccionario["nombre"] = "Gregory"
diccionario["edad"] = 20
#print(diccionario)

# Obtener valor vinculado a una llave
#print(diccionario["edad"])
#print(diccionario.get("edad"))

# Crear diccionario asignando valores desde un principio
diccionario2 ={5.1: 10 , "vocales":["a", "e", "i", "o", "u"], (7,2): 50 }
print(diccionario2)

# Len
#rint(len(diccionario2))

# del
del(diccionario2[(7,2)])
print(diccionario2)

