def nombreCompleto(nombres, apellidos):
    return f"{nombres} {apellidos}"

def nombreCompletoMayus(nombres, apellidos):
    return f"{nombres} {apellidos}".upper()

def nombreCompletoMin(nombres, apellidos):
    return f"{nombres} {apellidos}".lower()

def nombreCompletoCapitalizable(nombres, apellidos):
    return f"{nombres.capitalize()} {apellidos.capitalize()}"

def nombreCompletoTitulo(nombres, apellidos):
    return f"{nombres} {apellidos}".title()

def GenerarCorreo(nombres, apellidos):
    return f"{nombres[:3].lower()}.{apellidos[:3].lower()}@uamv.edu.ni"

nombres = input("Dime tu nombre: ")
apellidos = input("Dime tus apellidos: ")

print(nombreCompleto(nombres, apellidos))
print(nombreCompletoMayus(nombres, apellidos))
print(nombreCompletoMin(nombres, apellidos))
print(nombreCompletoCapitalizable(nombres, apellidos))
print(nombreCompletoTitulo(nombres, apellidos))
print(GenerarCorreo(nombres, apellidos))