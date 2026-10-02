#Cadena de Caracteres
nombre = "Martín Elise Castillo Hernández"

texto = "               "

print("Nombre:", end= " ")
print(nombre)
print("Texto:", end= " ")
print(texto)

#Tamaño de Cadena
print("Nombre:", end= " ")
print(len(nombre))
print("Texto:", end= " ")
print(len(texto))

texto += nombre
print("Nombre:", end= " ")
print(nombre)
print("Texto:", end= " ")
print(texto)


#Limpiar Espacio
print("Nombre:", end= " ")
print(nombre)
print("Texto:", end= " ")
print(texto.strip())