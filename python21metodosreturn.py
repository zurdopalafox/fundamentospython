def convertyirMayusculas(cadena):
    return cadena.upper()   

def convertyirMinusculas(cadena):
    return cadena.lower()   

def concatenarCadenas(cadena1, cadena2):
    return cadena1 + cadena2


resultado = convertyirMayusculas("hola")
print(resultado)
resultado = convertyirMinusculas(resultado)
print(resultado)
resultado = concatenarCadenas(resultado, " Mundo")
print(resultado)
resultado = concatenarCadenas(convertyirMayusculas(resultado), convertyirMinusculas(" PYTHON"))
print(resultado)

